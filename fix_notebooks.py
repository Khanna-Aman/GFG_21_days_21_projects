#!/usr/bin/env python3
"""
Fix notebook widget metadata issues by removing 'metadata.widgets' key
that is missing the required 'state' key.
"""

import json
import os
from pathlib import Path

def fix_notebook(notebook_path):
    """Fix a single notebook by removing problematic widget metadata."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Check if metadata.widgets exists and remove it
        modified = False
        if 'metadata' in notebook and 'widgets' in notebook['metadata']:
            # Remove the widgets metadata entirely
            del notebook['metadata']['widgets']
            modified = True
            print(f"✓ Fixed: {notebook_path}")
        
        # Save the notebook if modified
        if modified:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, indent=1, ensure_ascii=False)
            return True
        else:
            print(f"  Skipped (no widget metadata): {notebook_path}")
            return False
            
    except Exception as e:
        print(f"✗ Error fixing {notebook_path}: {e}")
        return False

def main():
    """Find and fix all notebooks in the repository."""
    root_dir = Path('.')
    
    # Find all .ipynb files, excluding checkpoints
    notebooks = []
    for notebook_path in root_dir.rglob('*.ipynb'):
        if '.ipynb_checkpoints' not in str(notebook_path):
            notebooks.append(notebook_path)
    
    print(f"Found {len(notebooks)} notebooks to check\n")
    
    fixed_count = 0
    for notebook_path in notebooks:
        if fix_notebook(notebook_path):
            fixed_count += 1
    
    print(f"\n{'='*60}")
    print(f"Summary: Fixed {fixed_count} out of {len(notebooks)} notebooks")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()

