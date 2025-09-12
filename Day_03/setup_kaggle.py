"""
Setup script for Kaggle API and Housing Dataset Download
This script helps set up the Kaggle API and download the required dataset.
"""

import os
import json
import subprocess
import sys
from pathlib import Path

def setup_kaggle_api():
    """Setup Kaggle API credentials"""
    print("=== Kaggle API Setup ===")
    print("\nTo download the housing dataset, you need to set up Kaggle API credentials.")
    print("\nSteps to get your Kaggle API key:")
    print("1. Go to https://www.kaggle.com/account")
    print("2. Scroll down to 'API' section")
    print("3. Click 'Create New Token'")
    print("4. This will download 'kaggle.json' file")
    print("5. Place the kaggle.json file in this directory (Day_03/)")
    
    # Check if kaggle.json exists in current directory
    kaggle_json_path = Path("kaggle.json")
    if kaggle_json_path.exists():
        print(f"\n✓ Found kaggle.json in current directory")
        
        # Create .kaggle directory in user home
        kaggle_dir = Path.home() / ".kaggle"
        kaggle_dir.mkdir(exist_ok=True)
        
        # Copy kaggle.json to the correct location
        import shutil
        target_path = kaggle_dir / "kaggle.json"
        shutil.copy2(kaggle_json_path, target_path)
        
        # Set proper permissions (important for security)
        if os.name != 'nt':  # Not Windows
            os.chmod(target_path, 0o600)
        
        print(f"✓ Copied kaggle.json to {target_path}")
        return True
    else:
        print(f"\n✗ kaggle.json not found in current directory")
        print("Please download kaggle.json from Kaggle and place it in Day_03/ folder")
        return False

def download_housing_dataset():
    """Download the housing dataset using Kaggle API"""
    print("\n=== Downloading Housing Dataset ===")
    
    try:
        # Create data directory
        data_dir = Path("data")
        data_dir.mkdir(exist_ok=True)
        
        # Download the dataset
        cmd = [
            sys.executable, "-m", "kaggle", "competitions", "download", 
            "-c", "house-prices-advanced-regression-techniques",
            "-p", "data"
        ]
        
        print("Downloading dataset...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✓ Dataset downloaded successfully")
            
            # Unzip the dataset
            import zipfile
            zip_path = data_dir / "house-prices-advanced-regression-techniques.zip"
            if zip_path.exists():
                print("Extracting files...")
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(data_dir)
                print("✓ Files extracted successfully")
                
                # Remove zip file
                zip_path.unlink()
                print("✓ Cleanup completed")
                
                return True
            else:
                print("✗ Zip file not found after download")
                return False
        else:
            print(f"✗ Download failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"✗ Error downloading dataset: {e}")
        return False

def verify_installation():
    """Verify that all required packages are installed"""
    print("\n=== Verifying Package Installation ===")
    
    required_packages = [
        'pandas', 'numpy', 'matplotlib', 'seaborn', 'scipy',
        'sklearn', 'xgboost', 'kaggle'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'sklearn':
                import sklearn
            else:
                __import__(package)
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Run: py -m pip install " + " ".join(missing_packages))
        return False
    else:
        print("\n✓ All required packages are installed!")
        return True

def main():
    """Main setup function"""
    print("🏠 Housing Market Prediction - Day 3 Setup")
    print("=" * 50)
    
    # Change to Day_03 directory
    os.chdir(Path(__file__).parent)
    
    # Verify package installation
    if not verify_installation():
        print("\n❌ Please install missing packages first")
        return
    
    # Setup Kaggle API
    if setup_kaggle_api():
        # Download dataset
        if download_housing_dataset():
            print("\n🎉 Setup completed successfully!")
            print("\nYou can now run the housing market prediction notebook.")
            print("The dataset files are available in Day_03/data/")
        else:
            print("\n⚠️  Kaggle API setup successful, but dataset download failed.")
            print("You may need to manually download the dataset from:")
            print("https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data")
    else:
        print("\n⚠️  Please set up Kaggle API credentials first.")
        print("Alternative: Download the dataset manually from Kaggle")

if __name__ == "__main__":
    main()
