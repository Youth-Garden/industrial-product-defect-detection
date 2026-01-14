# Medical Lesion Detection and Segmentation

Project Report - Computer Vision Course

## Project Overview

This project aims to develop a Deep Learning system for automatic detection and segmentation of skin lesions (melanoma) using the ISIC 2016 dataset.

**Key Technologies:**

- Python 3
- PyTorch (Deep Learning Framework)
- Segmentation Models PyTorch (U-Net Architecture)
- Albumentations (Image Augmentation)
- KaggleHub (Dataset Management)

## Environment Setup

Follow these steps to set up the development environment on Windows.

### 1. Prerequisites

Ensure you have Python installed (version 3.8 or higher).
You can check this by running:

```bash
python --version
```

### 2. Create Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

Open your specific terminal (Git Bash or Command Prompt) in the project directory:

```bash
# Using Python launcher
py -m venv .venv
```

This will create a hidden folder named `.venv` containing the isolated environment.

### 3. Activate the Environment

To start using this environment, you must activate it.

```bash
# On Windows (Git Bash):
source .venv/Scripts/activate

# On Windows (Command Prompt):
.\.venv\Scripts\activate
```

When activated, you should see `(.venv)` at the beginning of your command prompt.

### 4. Install Dependencies

Install all required libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Download Dataset

This project uses the ISIC 2016 dataset. We have provided a script to automatically download it using `kagglehub`.

Run the following command:

```bash
python download_data.py
```

This script will:

1. Download the dataset to your KaggleHub cache.
2. Save the path to `dataset_path.txt` for the notebook to read.

## Project Structure

- `index.ipynb`: The main notebook containing the code, experiments, and report content.
- `download_data.py`: Script to handle dataset downloading.
- `requirements.txt`: List of python dependencies.
- `.venv/`: Virtual environment directory (do not commit this).
- `dataset_path.txt`: Local configuration file pointing to your data.
