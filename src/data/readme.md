# Spam Email Classifier – Hybrid Machine Learning (Naive Bayes + SVM)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Machine Learning](https://img.shields.io/badge/ML-Naive%20Bayes%20%2B%20SVM-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Project Overview

Spam emails pose a major threat in digital communication, leading to phishing attacks, fraud, scams, and security breaches. This project builds an intelligent **Hybrid Machine Learning Model** that combines:

* **Naive Bayes**
* **Support Vector Machine (SVM)**

to classify emails into **Spam or Not Spam (Ham)** with higher accuracy than standalone models.

---

## 🧠 Key Features

* Hybrid ML model using voting mechanism
* Text preprocessing and TF–IDF feature extraction
* Multiple evaluation metrics
* Modular code structure (`src/` folder)
* Reproducible results

---

## 🗂 Project Structure

```
Spam-Email-Classifier/
│
├── src/
│   ├── hybrid_classifier.py
│   ├── preprocessing.py
│   └── model_training.py
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

## 📥 Dataset

The dataset for this project was downloaded from Kaggle:

* **Email Spam Dataset**

Place the downloaded CSV file inside:

```
data/
```

If not available, follow the instructions in `data/readme.md`.

---

## 🔧 Installation

Install dependencies using:

```
pip install -r requirements.txt
```

---

## ▶ Running the Project

Run the hybrid model from terminal:

```
python src/hybrid_classifier.py
```

OR run individual modules:

```
python src/model_training.py
```

---

## 📊 Evaluation Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

Visualizations and result screenshots are stored in:

```
results/
```

---

## 🧭 Future Improvements

* Deploy model using Flask web app
* Integrate deep learning (LSTM/BERT)
* Real-time spam detection system

---

## 👩‍💻 Author

**Chaitra D Murthy**
23BTRCA020

---

## 🛡 License

This project is open-source under the **MIT License**.
### Full Academic Report (12 Pages)
<div align="center">
  <a href="docs/AML_NEW.pdf">
    <img src="https://img.shields.io/badge/Report-12 Pages-blue?style=for-the-badge&logo=adobe-acrobat-reader" alt="Report"/>
  </a>
  <a href="docs/Spam-Email-Classifier-Naive-Bayes-and-SVM.pptx">
    <img src="https://img.shields.io/badge/Slides-Presentation-orange?style=for-the-badge&logo=microsoft-powerpoint" alt="Slides"/>
  </a>
</div>

<br>

**Key Highlights from the Report**
| Section                  | Summary                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| Introduction             | Spam wastes bandwidth, reduces productivity, enables phishing & fraud  |
| Prior Study              | Rule-based → outdated<br>Naïve Bayes → fast but word dependencies<br>SVM → strong margins<br>**Hybrid → best of both** |
| Problem Statement        | “Design & implement a hybrid NB+SVM system for accurate spam filtering” |
| Methodology              | Data cleaning → TF-IDF → Voting ensemble → 97.8% accuracy              |
| Results                  | Hybrid outperforms individual models (see table above)                   |

> Full 12-page report with references, flowcharts and detailed analysis is available in [`docs/AML_NEW.pdf`](docs/AML_NEW.pdf)
