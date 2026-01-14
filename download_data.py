
import kagglehub
import os
import shutil

def download_dataset():
    print("🚀 Bắt đầu tải dataset ISIC 2016 từ Kaggle Hub...")
    
    # Download latest version
    path = kagglehub.dataset_download("mahmudulhasantasin/isic-2016-original-dataset")
    
    print(f"✅ Dataset đã được tải về tại cache: {path}")
    
    print(f"✅ Dataset is ready at: {path}")
    
    # Create a config file to store the path for the notebook to use
    config_path = os.path.join(os.getcwd(), "dataset_path.txt")
    with open(config_path, "w") as f:
        f.write(path)
    print(f"📝 Đã lưu đường dẫn dataset vào file: {config_path}")
    print("� Bạn có thể dùng đường dẫn này trong Notebook.")

if __name__ == "__main__":
    download_dataset()
