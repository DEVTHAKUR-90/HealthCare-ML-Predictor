```
██╗  ██╗███████╗ █████╗ ██╗  ████████╗██╗  ██╗
██║  ██║██╔════╝██╔══██╗██║  ╚══██╔══╝██║  ██║
███████║█████╗  ███████║██║     ██║   ███████║
██╔══██║██╔══╝  ██╔══██║██║     ██║   ██╔══██║
██║  ██║███████╗██║  ██║███████╗██║   ██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═╝

        M L   D I S E A S E   P R E D I C T O R
```

<div align="center">

**Symptom-driven disease prediction powered by ensemble machine learning**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python)](https://python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

*Enter your symptoms. Get a prediction. Three models, one consensus.*

</div>

---

## Overview

**HealthCare ML Predictor** is a Streamlit web application that takes user-reported symptoms as input and predicts the most likely disease using three independent machine learning classifiers. Rather than relying on a single model's output, the system runs all three in parallel — giving you a more reliable, cross-validated result.

> ⚠️ **Disclaimer:** This tool is built for educational and research purposes. It is not a substitute for professional medical diagnosis or advice.

---

## How Prediction Works

```
  User Selects Symptoms
          │
          ▼
  ┌───────────────────────────────────────────┐
  │            Feature Encoding               │
  │   Symptoms mapped to binary feature vector│
  └───────────────────────────────────────────┘
          │
          ├──────────────┬──────────────┐
          ▼              ▼              ▼
  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
  │  Naive Bayes │ │Decision Tree │ │Random Forest │
  │  (Gaussian)  │ │  Classifier  │ │  Classifier  │
  └──────────────┘ └──────────────┘ └──────────────┘
          │              │              │
          └──────────────┴──────────────┘
                         │
                         ▼
              Combined Prediction Output
```

Each model independently classifies the symptom vector. Results are displayed together, letting you see where all three models agree — which is the strongest indicator of a likely condition.

---

## Models

| Model | Type | Strength |
|-------|------|----------|
| **Gaussian Naive Bayes** | Probabilistic | Fast, performs well on high-dimensional symptom data |
| **Decision Tree** | Rule-based | Interpretable, clear decision paths |
| **Random Forest** | Ensemble | Most robust — aggregates many decision trees |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **UI & App** | Streamlit |
| **Language** | Python 3.10+ |
| **ML Models** | scikit-learn |
| **Data Processing** | pandas, NumPy |

---

## Dataset

The training dataset is not included in this repository due to its size. Download it from the link below and place it in the root project folder before running.

📥 **[Download Dataset — Google Drive](https://drive.google.com/file/d/1CrOUwsoHVguL5oHcmtPblt3_6AAJHT9m/view?usp=drive_link)**

Once downloaded:

```
healthcare-ml-predictor/
├── m2.py
├── requirements.txt
├── dataset.csv        ← place it here
└── ...
```

---

## Getting Started

### Prerequisites

- Python `3.10+`
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/DEVTHAKUR-90/HealthCare-ML-Predictor.git
cd HealthCare-ML-Predictor

# Install dependencies
pip install -r requirements.txt
```

### Run

```bash
streamlit run m2.py
```

The app will open automatically at `http://localhost:8501`.

---

## Project Structure

```
healthcare-ml-predictor/
│
├── m2.py                  # Main Streamlit application
├── requirements.txt       # Python dependencies
├── dataset.csv            # Training data (download separately)
└── README.md
```

---

## Roadmap

- [x] Multi-model disease prediction
- [x] Streamlit web interface
- [x] Gaussian Naive Bayes, Decision Tree, Random Forest
- [ ] Model confidence scores and probability display
- [ ] Explainability layer (feature importance per prediction)
- [ ] Expanded symptom dataset
- [ ] REST API for external integration

---

## Author

**Dev Thakur**

Cybersecurity enthusiast and developer with a focus on intelligent systems, ML applications, and real-world problem solving.

[![GitHub](https://img.shields.io/badge/GitHub-DEVTHAKUR--90-181717?style=flat-square&logo=github)](https://github.com/DEVTHAKUR-90)

---

<div align="center">
  <sub>Built to explore the intersection of machine learning and healthcare — responsibly.</sub>
</div>
