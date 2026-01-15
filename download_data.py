
import kagglehub
import os
import shutil

def download_dataset():
    print("🚀 Starting NEU Surface Defect dataset download from Kaggle Hub...")
    
    # Download latest version
    path = kagglehub.dataset_download("kaustubhdikshit/neu-surface-defect-database")
    
    print(f"✅ Dataset downloaded to cache: {path}")
    
    # Create a config file to store the path for the notebook to use
    config_path = os.path.join(os.getcwd(), "dataset_path.txt")
    with open(config_path, "w") as f:
        f.write(path)
    print(f"📝 Dataset path saved to file: {config_path}")
    print("👉 You can use this path in the Notebook.")

if __name__ == "__main__":
    download_dataset()
