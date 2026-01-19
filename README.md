# Industrial Product Defect Detection (NEU Surface Defect)

## Project Overview

This project focuses on developing a Deep Learning system for automatic detection of surface defects on steel sheets (e.g., scratches, patches, pitted surfaces) using the NEU Surface Defect Database. The goal is to automate quality inspection in industrial production lines.

**Key Technologies:**

- Python 3
- PyTorch (Deep Learning Framework)
- Torchvision (Object Detection models - Faster R-CNN)
- Albumentations (Image Augmentation)

- KaggleHub (Dataset Management)

## Environment Setup

Follow these steps to set up the development environment on Windows.

### 1. Prerequisites

Ensure you have Python installed (version 3.8 or higher). You can check this by running:

```bash
python --version
```

### 2. Create Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

Open your terminal in the project directory:

```bash
# Using Python launcher
py -m venv .venv
```

### 3. Install Dependencies

Activate the virtual environment and install the required packages:

```bash
# Activate virtual environment
source .venv/Scripts/activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

### 4. Download Dataset

Run the `download_data.py` script to download the NEU Surface Defect Database and set up the dataset path:

```bash
python download_data.py
```

This will create a `dataset_path.txt` file containing the path to the dataset.

### 5. Run the Notebook

Open the `index.ipynb` notebook in Jupyter Notebook or VS Code and execute the cells sequentially to:

1. **Train the model**: Follow the steps in Chapter 5 to train the Faster R-CNN model.
2. **Evaluate the model**: Use the evaluation cells in Chapter 5.2 to calculate metrics like mAP, Precision, and Recall.
3. **Visualize results**: Use the visualization cells in Chapter 5.3 to display predictions and bounding boxes on test images.
