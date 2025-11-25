# 📧 Hybrid Spam Email Classifier (Naive Bayes + SVM)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Machine Learning](https://img.shields.io/badge/Model-Naive%20Bayes%20%2B%20SVM-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🔗 Open in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](PASTE_YOUR_COLAB_LINK_HERE)

---

## 📑 Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Architecture](#architecture)
* [Dataset](#dataset)
* [Technologies Used](#technologies-used)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Running the Project](#running-the-project)
* [Results](#results)
* [Future Improvements](#future-improvements)
* [Screenshots](#screenshots)
* [Author](#author)
* [License](#license)

---

## 📌 Project Overview

Spam emails are a major security threat in digital communication, often resulting in phishing, fraud, data loss, and financial damage.

This project builds a **Hybrid Machine Learning Model** that combines:

* **Naive Bayes**
* **Support Vector Machine (SVM)**

Using a voting mechanism, the hybrid model achieves **higher accuracy and lower false-positive rates** compared to individual models.

---

## ✨ Features

✔ Hybrid classification using NB + SVM
✔ Text preprocessing (stopword removal, tokenization, cleaning)
✔ TF-IDF feature extraction
✔ Model evaluation metrics
✔ Modular Python implementation
✔ Ready to run in Google Colab
✔ Dataset included

---

## 🧠 Architecture

```
           ┌────────────┐
           │ Raw Emails │
           └──────┬─────┘
                  │
        Text Cleaning & Tokenization
                  │
            TF-IDF Vectorizer
                  │
       ┌──────────┴─────────┐
       │                    │
Naive Bayes Model      SVM Model
       │                    │
       └──────────┬─────────┘
          Hybrid Voting System
                  │
          Final Email Classification
```

---

## 📥 Dataset

This project uses the **Email Spam Dataset downloaded from Kaggle**.

Place the CSV file inside:

```
data/
```

If the dataset is missing, follow instructions in `data/readme.md`.

---

## 🧾 Technologies Used

* Python
* Scikit-Learn
* Pandas
* NumPy
* NLTK
* Matplotlib
* Seaborn

---

## 📂 Project Structure

```
Spam-Email-Classifier/
│
├── src/
│   ├── preprocessing.py
│   ├── model_training.py
│   ├── hybrid_classifier.py
│
├── data/
│   └── readme.md
│
├── results/
│   └── readme.md
│
├── docs/
│   ├── report.pdf
│   └── presentation.pptx
│
├── requirements.txt
└── README.md
```

---

## 🔧 Installation

Install the dependencies:

```
pip install -r requirements.txt
```

---

## ▶ Running the Project

### Run the hybrid model:

```
python src/hybrid_classifier.py
```

### Or run model training only:

```
python src/model_training.py
```

### Or open in Google Colab:

Click the Colab button at the top.

---

## 📊 Results

The hybrid model provides:

* Higher accuracy
* Reduced false detections
* Stronger stability
* Robust performance across datasets

Evaluation metrics include:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

Graphs and screenshots are stored inside:

```
/results
```

---

## 🖼 Screenshots

> Add your visual outputs here (confusion matrix, accuracy plot, output samples)
> <img width="935" height="478" alt="image" src="https://github.com/user-attachments/assets/b142a17f-b59d-43f0-afd2-c948afd9a05d" />
<img width="742" height="585" alt="image" src="https://github.com/user-attachments/assets/a11d88a7-930d-4ff2-a0b9-864d8b522fdd" />



Example:

```
results/confusion_matrix.png
results/accuracy_plot.png
```

---

## 🧭 Future Improvements

* Deploy on Flask or Streamlit
* Add LSTM / BERT deep learning models
* Real-time email scanning system
* SQL or Firebase storage backend

---

## 👩‍💻 Author

**Chaitra D Murthy**
USN: 23BTRCA020

---

## 🛡 License

Distributed under the MIT License.

