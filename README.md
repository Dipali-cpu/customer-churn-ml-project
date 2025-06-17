# 🧠 Customer Churn Prediction - ML Pipeline Project

This project predicts whether a customer will churn (i.e., leave) based on demographic and service-related features using a complete **Machine Learning Pipeline** and deploys the model as a web app using **Streamlit**.

---

## 📌 Project Structure


---
## 🔍 Dataset

- Contains features like gender, tenure, services used, contract type, payment method, etc.
- Target: `Churn` (Yes/No)
---
## ⚙️ Machine Learning Flow

1. **Preprocessing:**

   - Handling missing values
   - One-hot encoding for categoricals
   - Feature scaling for numericals
2. **Pipeline:**

   - `ColumnTransformer` + `Pipeline` from `sklearn`
   - `RandomForestClassifier`
3. **Model Evaluation:**

   - Classification report
   - Confusion matrix
   - Accuracy, Precision, Recall, F1
4. **Deployment:**

   - `Streamlit` frontend
   - `pickle` to load trained model
   - Web interface for user input and prediction

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/customer_churn_ml_project.git
cd customer_churn_ml_project

# (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run churn_app.py
```
