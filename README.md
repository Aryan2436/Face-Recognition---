# Eigenfaces Face Recognition Lab

This repository contains a Jupyter/Google Colab notebook demonstrating the **Eigenfaces approach to face analysis using Principal Component Analysis (PCA)**.

The notebook covers image loading and preprocessing, mean-face calculation, image normalization, PCA feature extraction, eigenface visualization, and explained-variance analysis.

## Repository Contents

```text
.
├── Face_Recognition.ipynb
├── Class_Images.zip                 # Dataset archive (provide separately)
└── README.md
```

> The notebook expects the dataset archive to be named `Class_Images.zip`. Update the upload step if your archive has a different name.

## Dataset Structure

After extracting `Class_Images.zip`, the notebook expects this folder structure:

```text
data/
└── class_images/
    ├── nonsmiling_cropped/   # Images used as training data
    └── smiling_cropped/      # Images used as testing data
```

The images are read in grayscale, resized to **64 × 64 pixels**, and flattened into one-dimensional feature vectors. The filename (without its extension) is stored as the image label.

Make sure the archive contains the folders above. The dataset is not embedded in the notebook, so it must be supplied separately.

## Requirements

The notebook uses:

- Python 3
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Plotly
- OpenCV (`opencv-python`)
- Scikit-learn

Install the libraries locally with:

```bash
pip install numpy pandas matplotlib seaborn plotly opencv-python scikit-learn
```

## How to Run

### Option 1: Google Colab

1. Upload `Face_Recognition.ipynb` to Google Colab.
2. Run the import cells.
3. When prompted, upload `Class_Images.zip`.
4. Run the remaining cells in order.
5. Review the generated face images, mean face, eigenfaces, and explained-variance plot.

### Option 2: Jupyter Notebook

1. Clone or download this repository.
2. Install the required libraries.
3. Extract the dataset so that it follows the folder structure shown above.
4. If running outside Google Colab, replace the `google.colab.files.upload()` dataset-upload cell with a local path to `Class_Images.zip` (or extract the archive manually into the expected `data/` directory).
5. Open `Face_Recognition.ipynb` and run all cells from top to bottom.

## Notebook Workflow

1. **Import libraries** – Load the Python libraries used for image processing, numerical operations, visualization, and PCA.
2. **Load the dataset** – Upload and extract the ZIP archive.
3. **Prepare images** – Read training images from `nonsmiling_cropped` and testing images from `smiling_cropped`.
4. **Preprocess images** – Convert images to grayscale, resize them to 64 × 64, and flatten them into vectors.
5. **Visualize sample images** – Display sample training and testing images with their filename-based labels.
6. **Calculate the mean face** – Compute the average of the training image vectors.
7. **Normalize images** – Subtract the mean face from the training and testing image vectors.
8. **Apply PCA** – Fit PCA with 30 components on the normalized training data and transform the testing data.
9. **Visualize eigenfaces** – Display the principal components as 64 × 64 eigenface images.
10. **Analyze explained variance** – Plot the explained-variance ratio for the selected components.

## Output

Running the notebook produces:

- Sample training and testing face images
- The calculated mean face
- A comparison of an original image, mean face, and normalized image
- Training and testing PCA feature matrices
- Visualizations of the first ten eigenfaces
- A plot showing the explained variance ratio of the 30 PCA components

## Important Note

This notebook demonstrates **PCA-based Eigenfaces feature extraction and visualization**. It does not currently implement a complete face-identification or face-classification stage: there is no classifier, matching-distance calculation, prediction step, or recognition-accuracy evaluation in the notebook.

## Technologies Used

`Python` · `NumPy` · `Pandas` · `OpenCV` · `Matplotlib` · `Seaborn` · `Plotly` · `Scikit-learn`

## Author

Add your name and any course/lab details here.
