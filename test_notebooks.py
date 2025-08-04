#!/usr/bin/env python3
"""
Simple validation script to check if the notebooks can be loaded and basic imports work.
This is a minimal test to ensure the notebooks are properly formatted.
"""

import json
import sys
import importlib

def test_notebook_structure(notebook_path):
    """Test if notebook has valid structure"""
    try:
        with open(notebook_path, 'r') as f:
            nb = json.load(f)
        
        assert 'cells' in nb, "No cells found in notebook"
        assert len(nb['cells']) > 0, "Notebook is empty"
        
        code_cells = [cell for cell in nb['cells'] if cell['cell_type'] == 'code']
        markdown_cells = [cell for cell in nb['cells'] if cell['cell_type'] == 'markdown']
        
        assert len(code_cells) > 10, "Not enough code cells"
        assert len(markdown_cells) > 5, "Not enough markdown cells"
        
        print(f"✓ {notebook_path}: Valid structure ({len(code_cells)} code, {len(markdown_cells)} markdown)")
        return True
    except Exception as e:
        print(f"✗ {notebook_path}: {e}")
        return False

def test_basic_imports():
    """Test if basic required packages can be imported"""
    required_packages = [
        'pandas', 'numpy', 'matplotlib', 'seaborn', 
        'sklearn', 'joblib'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✓ {package}: Available")
        except ImportError:
            missing_packages.append(package)
            print(f"✗ {package}: Not available")
    
    if missing_packages:
        print(f"\nNote: {len(missing_packages)} packages not available in current environment")
        print("This is normal - packages will be installed automatically in Google Colab")
    
    return len(missing_packages) == 0

def main():
    """Main test function"""
    print("Testing Automated ML Notebooks...\n")
    
    # Test notebook structures
    notebooks = [
        'Automated_Classification_ML.ipynb',
        'Automated_Regression_ML.ipynb'
    ]
    
    all_valid = True
    for notebook in notebooks:
        if not test_notebook_structure(notebook):
            all_valid = False
    
    print("\nTesting basic imports...")
    test_basic_imports()
    
    if all_valid:
        print("\n🎉 All notebooks are properly structured and ready for use!")
        print("You can now upload them to Google Colab and start using automated ML!")
        return 0
    else:
        print("\n❌ Some notebooks have structural issues")
        return 1

if __name__ == "__main__":
    sys.exit(main())