# CODE STRUCTURE & WORKFLOW GUIDE

This document explains the project structure, code components, and most importantly, the **dependency workflow** between code sections in the `index.ipynb` Notebook to ensure error-free execution.

## 1. Project Structure Overview

- `requirements.txt`: List of libraries to install.
- `download_data.py`: Script to download the dataset from Kaggle. Run this **first** to get the data.
- `dataset_path.txt`: Text file containing the path to the dataset folder (created by the above script).
- `index.ipynb`: Main code file (Notebook Report).
- `best_model.pth`: File containing the best model weights (created after running Training in Chapter 5).

---

## 2. Workflow in Notebook (`index.ipynb`)

The Notebook is designed to run sequentially from top to bottom. Here are the key dependencies:

### 🔰 **Step 1: Initialization (Chapter 0)**

- **Code:** Library Import Cell & Constants Cell.
- **Task:** Load libraries, set seed, device (CPU/GPU), and **READ DATASET PATH** from `dataset_path.txt`.
- **⚠️ Note:** If you don't run this cell, subsequent sections will report errors about missing libraries or dataset paths.

### 🔰 **Step 2: Dataset & Dataloader (Chapter 3)**

- **Code:** `NEUDataset` Class, Transforms, `visualize_batch`.
- **Task:**
  - Read images and bounding boxes from the disk.
  - Create variables `train_dataset`, `test_dataset`.
  - Create **`train_loader`** and **`test_loader`**.
- **⚠️ DEPENDENCY:**
  - Requires `DATASET_PATH` from Step 1.
  - **IMPORTANT:** The variables `train_loader` and `test_loader` created here are used directly in the **Training Loop (Chapter 5)**. Skipping this step will cause Chapter 5 to fail.

### 🔰 **Step 3: Model (Chapter 4)**

- **Code:** Initialize Faster R-CNN model.
- **Task:** Load Faster R-CNN architecture and fine-tune it for the NEU dataset.
- **⚠️ DEPENDENCY:**
  - The variable `model` created here is the "main character" to be trained in Chapter 5.

### 🔰 **Step 4: Training (Chapter 5.1)**

- **Code:** Loss Function, Optimizer, `train_fn`, `eval_fn`, Epoch Loop.
- **Task:**
  - Use `train_loader` (from Step 2) to teach the model.
  - Use `test_loader` (from Step 2) to test the model.
  - Update weights for `model` (from Step 3).
  - **SAVE FILE:** Automatically save the best model to `best_model.pth`.
- **⚠️ PENDING STATUS:**
  - This section takes a while to run (depending on GPU).
  - After running, it creates the `best_model.pth` file. This file is REQUIRED for **Visualization (5.2)**.

### 🔰 **Step 5: Visualization & Evaluation (Chapter 5.2 & Chapter 6)**

- **Code:** Load `best_model.pth`, calculate mAP/Precision/Recall, visualize predictions.
- **⚠️ DEPENDENCY:**
  - Requires `best_model.pth` (result of Step 4).
  - Requires `test_loader` (from Step 2) to get test data.

---

## 3. Dependency Summary Table

| Code Section              | Created Variable (Output)                  | Used In (Input For)                   | Status             |
| :------------------------ | :----------------------------------------- | :------------------------------------ | :----------------- |
| **Chapter 0 (Constants)** | `DATASET_PATH`, `DEVICE`                   | Chapter 3, 4, 5, 5.2                  | ✅ Done            |
| **Chapter 3 (Dataset)**   | **`train_loader`**, **`test_loader`**      | **Chapter 5 (Training)**, Chapter 5.2 | ✅ Done            |
| **Chapter 4 (Model)**     | **`model`**                                | **Chapter 5 (Training)**              | ⏳ Code Incomplete |
| **Chapter 5 (Training)**  | File **`best_model.pth`**, Trained `model` | **Chapter 5.2 (Visual / Evaluation)** | ⏳ Code Incomplete |
| **Chapter 5.2 (Results)** | Charts, Demo Images, mAP Metrics           | Final Report                          | ⏳ Code Incomplete |

---

## 💡 Quick Debug Tip

If you encounter a `NameError` (e.g., `name 'train_loader' is not defined`), it means you **forgot to run** (or ran with errors) the code cell that creates that variable in previous chapters. Go back and run sequentially from top to bottom!
