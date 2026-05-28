# 📉 Customer Churn Prediction

> End-to-end ML pipeline that predicts telecom customer churn — with a live interactive web app.

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Click_Here-238636?style=for-the-badge)](https://customer-churn-ml-project-26igffygpgvonfupy3kh9d.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML_Pipeline-f7931e?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-2ea043?style=for-the-badge)](LICENSE)

---

## 🌐 Live Demo

**[👉 Try the live app →](https://customer-churn-ml-project-26igffygpgvonfupy3kh9d.streamlit.app/)**

## 📸 Screenshots

![Stay Prediction](assets/churn_stay.png)
![Churn Prediction](assets/churn_predict.png)

Enter customer details and get an instant churn prediction with probability score.

---
## 📊 Model Performance

| Metric | Score |
|--------|-------|
| ✅ Accuracy | **78%** |
| 🎯 ROC-AUC Score | **81.9%** |
| 🔁 CV ROC-AUC | **81.8% ± 1.3%** |
| 🎯 Precision (Churn) | **63%** |
| 🔁 Recall (Churn) | **47%** |
| ⚖️ F1 Score (Churn) | **54%** |

> Model evaluated on 1,409 test samples. Cross-validated across 5 folds.

---

## 💡 What This Project Does

A complete machine learning solution for predicting which telecom customers are likely to cancel their subscription. Takes 19 customer features as input and outputs a **churn probability** with key risk indicators — helping businesses take proactive retention action.

**Business impact:** Reducing churn by even 1% in a telecom company with 1M customers saves millions in revenue. This model gives the retention team a prioritised list of at-risk customers to act on.

---

## 🔧 ML Pipeline

| Stage | Details |
|-------|---------|
| 📁 Data | Telco Customer Churn dataset — 7,043 rows, 21 features |
| 🧹 Preprocessing | Missing value handling, one-hot encoding (categoricals), standard scaling (numericals) via `ColumnTransformer` |
| 🤖 Model | `RandomForestClassifier` inside a full `sklearn` `Pipeline` |
| 📈 Evaluation | Accuracy, Precision, Recall, F1-Score, Confusion Matrix |
| 🚀 Deployment | Model serialized with `pickle`, served via Streamlit web app |

---

## ✨ App Features

- Enter customer details via sidebar (tenure, contract type, services, payment method, etc.)
- Instant **Churn / No Churn** prediction
- Churn **probability score** displayed
- Clean, intuitive UI — no technical knowledge needed

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| ML | Scikit-learn (Pipeline, ColumnTransformer, RandomForestClassifier) |
| Frontend | Streamlit |
| Data | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Deployment | Streamlit Community Cloud |

---

## 📂 Project Structure

```
customer-churn-ml-project/
├── churn_pipeline.py      # Model training + pipeline building
├── churn_app.py           # Streamlit web app (frontend)
├── churn_pipeline.pkl     # Trained model (serialized with pickle)
├── WA_Fn-UseC_-Telco-Customer-Churn.csv   # Dataset
├── requirements.txt       # Dependencies
└── README.md
```

---

## 🚀 Run Locally

```bash
git clone https://github.com/Dipali-cpu/customer-churn-ml-project.git
cd customer-churn-ml-project
pip install -r requirements.txt
streamlit run churn_app.py
```

To retrain the model:
```bash
python churn_pipeline.py
```

---

## 🎯 Key Technical Decisions

- **sklearn Pipeline** — preprocessing and model are bundled together, so the same transformations apply at prediction time automatically (no data leakage)
- **ColumnTransformer** — handles numeric and categorical columns separately in one clean step
- **pickle serialization** — trained model saved to disk so the app loads instantly without retraining
- **Random Forest** — chosen for its robustness to imbalanced classes and interpretability via feature importance

---

## 👩‍💻 Built by

**Dipali** — Data Science & Analytics professional  
Self-taught in Python, Machine Learning, SQL, and end-to-end ML deployment.  
Completed Data Science internship · April 2026

[![LinkedIn](https://img.shields.io/badge/Connect_on-LinkedIn-0077b5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/dipali-chothmal-5731b032b/)
[![GitHub](https://img.shields.io/badge/More_Projects-GitHub-333?style=flat-square&logo=github)](https://github.com/Dipali-cpu)

---

## 📄 License

MIT License — free to use, modify, and distribute.
