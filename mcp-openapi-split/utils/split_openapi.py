#!/usr/bin/env python3
"""
Split DolphinScheduler OpenAPI specification into multiple smaller files.
"""
import json
import os
import re
from collections import defaultdict

# Input file
INPUT_FILE = '../ds-restfuleapi-v1.json'

# Output directories
BASE_DIR = 'base'
PATHS_DIR = 'paths'
SCHEMAS_DIR = 'schemas'
COMBINED_DIR = 'combined'

def ensure_directories():
    """Ensure all necessary directories exist."""
    for directory in [BASE_DIR, PATHS_DIR, SCHEMAS_DIR, COMBINED_DIR]:
        os.makedirs(directory, exist_ok=True)

def load_openapi():
    """Load the OpenAPI JSON file."""
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filename):
    """Save JSON data to a file with nice formatting."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_base_info(openapi):
    """Save the base OpenAPI information."""
    base_info = {
        "openapi": openapi["openapi"],
        "info": openapi["info"],
        "servers": openapi["servers"]
    }
    save_json(base_info, os.path.join(BASE_DIR, "01_base.json"))

def group_paths_by_tag(openapi):
    """Group API paths by their tags."""
    tag_paths = defaultdict(dict)
    
    # Group paths by the first tag
    for path, path_item in openapi["paths"].items():
        tag = None
        
        # Find the first operation with tags
        for method, operation in path_item.items():
            if "tags" in operation and operation["tags"]:
                tag = operation["tags"][0]
                break
        
        # If no tag found, use "misc"
        if not tag:
            tag = "misc"
        
        # Add to the appropriate tag group
        tag_paths[tag][path] = path_item
    
    return tag_paths

def save_paths_by_tag(tag_paths):
    """Save path groups to separate files."""
    for i, (tag, paths) in enumerate(sorted(tag_paths.items()), 1):
        # Create safe filename from tag
        safe_name = re.sub(r'[^a-zA-Z0-9]', '_', tag)
        filename = f"{i:02d}_{safe_name}.json"
        
        # Create the paths document
        paths_doc = {"paths": paths}
        save_json(paths_doc, os.path.join(PATHS_DIR, filename))
        
        print(f"Created path file {filename} with {len(paths)} paths for tag '{tag}'")

def group_schemas(openapi):
    """Group schemas into related categories."""
    schemas = openapi["components"]["schemas"]
    
    # Group 1: Basic result schemas
    result_schemas = {k: v for k, v in schemas.items() if k.startswith("Result")}
    
    # Group 2: Data models directly related to projects
    project_schemas = {k: v for k, v in schemas.items() if "Project" in k or "project" in k.lower()}
    
    # Group 3: Data models for tasks and workflows
    task_schemas = {k: v for k, v in schemas.items() if "Task" in k or "task" in k.lower()}
    workflow_schemas = {k: v for k, v in schemas.items() if "Process" in k or "Workflow" in k}
    
    # Group 4: User and tenant related
    user_schemas = {k: v for k, v in schemas.items() if "User" in k or "user" in k.lower()}
    tenant_schemas = {k: v for k, v in schemas.items() if "Tenant" in k or "tenant" in k.lower()}
    
    # Group 5: Resource and data source related
    resource_schemas = {k: v for k, v in schemas.items() if "Resource" in k or "resource" in k.lower()}
    datasource_schemas = {k: v for k, v in schemas.items() if "DataSource" in k or "datasource" in k.lower()}
    
    # Group 6: Alert and monitoring related
    alert_schemas = {k: v for k, v in schemas.items() if "Alert" in k or "alert" in k.lower()}
    
    # Group 7: K8s related
    k8s_schemas = {k: v for k, v in schemas.items() if "K8s" in k or "k8s" in k.lower()}
    
    # Group 8: Queue and worker related
    queue_schemas = {k: v for k, v in schemas.items() if "Queue" in k or "queue" in k.lower()}
    worker_schemas = {k: v for k, v in schemas.items() if "Worker" in k or "worker" in k.lower()}
    
    # Group 9: Environment and cluster related
    env_schemas = {k: v for k, v in schemas.items() if "Environment" in k or "environment" in k.lower()}
    cluster_schemas = {k: v for k, v in schemas.items() if "Cluster" in k or "cluster" in k.lower()}
    
    # Group 10: Schedule related
    schedule_schemas = {k: v for k, v in schemas.items() if "Schedule" in k or "schedule" in k.lower()}
    
    # Collect all allocated schemas
    allocated_schemas = set()
    for schema_group in [
        result_schemas, project_schemas, task_schemas, workflow_schemas,
        user_schemas, tenant_schemas, resource_schemas, datasource_schemas,
        alert_schemas, k8s_schemas, queue_schemas, worker_schemas,
        env_schemas, cluster_schemas, schedule_schemas
    ]:
        allocated_schemas.update(schema_group.keys())
    
    # Remaining schemas
    remaining_schemas = {k: v for k, v in schemas.items() if k not in allocated_schemas}
    
    # Split remaining schemas into smaller chunks
    remaining_chunks = {}
    chunk_size = len(remaining_schemas) // 10
    chunk_size = max(chunk_size, 1)
    
    chunk_id = 1
    current_chunk = {}
    
    for i, (key, value) in enumerate(remaining_schemas.items(), 1):
        current_chunk[key] = value
        if i % chunk_size == 0 or i == len(remaining_schemas):
            remaining_chunks[f"remaining_{chunk_id}"] = current_chunk
            chunk_id += 1
            current_chunk = {}
    
    # Prepare the final grouped schemas
    grouped_schemas = {
        "result": result_schemas,
        "project": project_schemas,
        "task": task_schemas,
        "workflow": workflow_schemas,
        "user": user_schemas,
        "tenant": tenant_schemas,
        "resource": resource_schemas,
        "datasource": datasource_schemas,
        "alert": alert_schemas,
        "k8s": k8s_schemas,
        "queue": queue_schemas,
        "worker": worker_schemas,
        "environment": env_schemas,
        "cluster": cluster_schemas,
        "schedule": schedule_schemas,
    }
    
    # Add the remaining chunks
    grouped_schemas.update(remaining_chunks)
    
    return grouped_schemas

def save_schemas(grouped_schemas):
    """Save schema groups to separate files."""
    for i, (group_name, schemas) in enumerate(sorted(grouped_schemas.items()), 1):
        # Create the schema document
        schema_doc = {"components": {"schemas": schemas}}
        
        # Save to a file
        filename = f"{i:02d}_{group_name}_schemas.json"
        save_json(schema_doc, os.path.join(SCHEMAS_DIR, filename))
        
        print(f"Created schema file {filename} with {len(schemas)} schemas for group '{group_name}'")

def create_combiner_script():
    """Create a script to combine all JSON files back into a single OpenAPI spec."""
    script_content = """#!/usr/bin/env python3
'''
Combine split OpenAPI files back into a single specification.
'''
import json
import os
import glob

# Output file
OUTPUT_FILE = '../combined_openapi.json'

def load_json(filename):
    '''Load JSON from a file.'''
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def combine_openapi():
    '''Combine all the split OpenAPI files into a single specification.'''
    # Start with the base information
    base_files = sorted(glob.glob('../base/*.json'))
    if not base_files:
        raise FileNotFoundError("No base files found!")
    
    combined = load_json(base_files[0])
    combined['paths'] = {}
    combined['components'] = {'schemas': {}}
    
    # Add all paths
    path_files = sorted(glob.glob('../paths/*.json'))
    for path_file in path_files:
        paths_data = load_json(path_file)
        if 'paths' in paths_data:
            combined['paths'].update(paths_data['paths'])
    
    # Add all schemas
    schema_files = sorted(glob.glob('../schemas/*.json'))
    for schema_file in schema_files:
        schema_data = load_json(schema_file)
        if 'components' in schema_data and 'schemas' in schema_data['components']:
            combined['components']['schemas'].update(schema_data['components']['schemas'])
    
    # Save the combined specification
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(combined, f, ensure_ascii=False, indent=4)
    
    print(f"Combined OpenAPI specification saved to {OUTPUT_FILE}")
    print(f"Specification contains {len(combined['paths'])} paths and {len(combined['components']['schemas'])} schemas")

if __name__ == '__main__':
    combine_openapi()
"""
    
    with open(os.path.join("utils", "combine_openapi.py"), 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    # Make the script executable
    os.chmod(os.path.join("utils", "combine_openapi.py"), 0o755)

def main():
    """Split the OpenAPI specification into multiple files."""
    # Ensure directories exist
    ensure_directories()
    
    # Load the OpenAPI spec
    print("Loading OpenAPI specification...")
    openapi = load_openapi()
    
    # Save base information (already done manually, but included for completeness)
    # save_base_info(openapi)
    print("Base information already saved manually")
    
    # Group and save paths by tag
    print("\nSplitting API paths by tags...")
    tag_paths = group_paths_by_tag(openapi)
    save_paths_by_tag(tag_paths)
    
    # Group and save schemas
    print("\nSplitting schema definitions...")
    grouped_schemas = group_schemas(openapi)
    save_schemas(grouped_schemas)
    
    # Create the combiner script
    print("\nCreating the combiner script...")
    create_combiner_script()
    
    print("\nDone! The OpenAPI specification has been split into multiple files.")
    print(f"Paths: {sum(len(paths) for paths in tag_paths.values())} paths in {len(tag_paths)} files")
    print(f"Schemas: {sum(len(schemas) for schemas in grouped_schemas.values())} schemas in {len(grouped_schemas)} files")

if __name__ == "__main__":
    main() 