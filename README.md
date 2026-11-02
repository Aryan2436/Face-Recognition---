<div align="center">

# 👤 Eigenfaces Face Recognition

### PCA-Based Face Feature Extraction & Visualization

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-Image%20Processing-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/Scikit--learn-PCA-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">
</p>

**A hands-on implementation of the Eigenfaces technique using Principal Component Analysis (PCA).**

</div>

---

## 📌 About the Project

This project demonstrates how facial images can be processed and represented using the **Eigenfaces method**. It uses **Principal Component Analysis (PCA)** to reduce image dimensionality and extract important facial features.

The notebook loads face images, preprocesses them, calculates the mean face, applies PCA, and visualizes the resulting eigenfaces and explained variance.

> **Project scope:** The current notebook focuses on PCA-based feature extraction and visualization. It does not yet include a complete face-matching or classification system.

---

## ✨ Key Features

<table>
  <tr>
    <td>🖼️ <b>Image Loading</b><br>Loads face images from the supplied dataset.</td>
    <td>⚙️ <b>Preprocessing</b><br>Converts images to grayscale and resizes them to 64 × 64.</td>
  </tr>
  <tr>
    <td>➗ <b>Mean Face</b><br>Calculates the average face from the training images.</td>
    <td>🧠 <b>PCA Analysis</b><br>Extracts 30 principal components from normalized images.</td>
  </tr>
  <tr>
    <td>👁️ <b>Eigenface Display</b><br>Visualizes the principal components as face images.</td>
    <td>📊 <b>Variance Analysis</b><br>Plots the explained variance ratio.</td>
  </tr>
</table>

---

## 🛠️ Technologies Used

| Technology | Purpose |
|:--|:--|
| Python | Main programming language |
| NumPy | Numerical operations and arrays |
| Pandas | Data handling |
| OpenCV | Image loading and processing |
| Matplotlib | Image and graph visualization |
| Seaborn | Data visualization |
| Plotly | Interactive visualization library |
| Scikit-learn | Principal Component Analysis (PCA) |

---

## 📂 Project Structure

```text
Eigenfaces-Face-Recognition/
│
├── Face_Recognition.ipynb
├── Class_Images.zip
└── README.md
```

### Dataset folder structure

After extracting `Class_Images.zip`, arrange the dataset as follows:

```text
data/
└── class_images/
    ├── nonsmiling_cropped/
    └── smiling_cropped/
```

- `nonsmiling_cropped/` — training images
- `smiling_cropped/` — testing images

The dataset archive must be supplied separately; it is not embedded in the notebook.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace the repository URL with your actual GitHub repository URL.

### 2. Install dependencies

```bash
pip install numpy pandas matplotlib seaborn plotly opencv-python scikit-learn
```

### 3. Prepare the dataset

Place `Class_Images.zip` where the notebook can access it.

The notebook currently uses Google Colab's file-upload feature. If you run it locally in Jupyter, replace that upload cell with a local dataset path or extract the archive into the expected folder structure.

### 4. Run the notebook

Open `Face_Recognition.ipynb` in **Google Colab** or **Jupyter Notebook**, then execute the cells in order.

---

## 🔬 How It Works

| Step | Process | Description |
|:--:|:--|:--|
| 01 | Import libraries | Loads the required Python packages. |
| 02 | Load dataset | Uploads and extracts the image archive. |
| 03 | Preprocess images | Converts images to grayscale and resizes them to 64 × 64 pixels. |
| 04 | Flatten images | Converts each image into a one-dimensional vector. |
| 05 | Calculate mean face | Computes the average training image. |
| 06 | Normalize images | Subtracts the mean face from each image vector. |
| 07 | Apply PCA | Fits PCA with 30 components on the training data. |
| 08 | Visualize eigenfaces | Displays principal components as 64 × 64 images. |
| 09 | Analyze variance | Plots the explained variance ratio. |

---

## 📈 Expected Outputs

After running the notebook, you should see:

- Sample training and testing face images
- The calculated mean face
- Original, mean, and normalized image comparisons
- PCA feature matrices for training and testing data
- Visualizations of the first ten eigenfaces
- Explained-variance plot for the 30 PCA components

---

## ▶️ Run in Google Colab

<div align="center">

<a href="https://colab.research.google.com/" target="_blank">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Google Colab">
</a>

<p><i>Upload the notebook to Colab, provide the dataset when prompted, and run the cells.</i></p>

</div>

---

## 🔮 Future Improvements

- Add a face-matching method using PCA feature vectors.
- Implement a classifier for face identification.
- Evaluate the model using suitable accuracy metrics.
- Test the approach with additional face images.

---

## 👨‍💻 Author

**Your Name**

- GitHub: [Aryan2436](https://github.com/Aryan2436)

---

<div align="center">

### ⭐ If you find this project useful, consider giving the repository a star!

<sub>Built with Python, OpenCV, and Scikit-learn.</sub>

</div>
