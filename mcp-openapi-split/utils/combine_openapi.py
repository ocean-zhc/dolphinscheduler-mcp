#!/usr/bin/env python3
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
