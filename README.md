# 🔮 Customer Churn Prediction App

A machine learning web application that predicts whether a telecom customer is likely to churn, built with  **Scikit-learn** ,  **Streamlit** , and visualized through a **Power BI Dashboard** for business insights.

---

## 📌 Project Overview

Customer churn is one of the most critical problems in the telecom industry. Losing a customer costs **5–7x more** than retaining one. This project builds an end-to-end ML pipeline that:

* Trains a **Random Forest Classifier** on real Telco customer data
* Predicts churn probability for any new customer in real time
* Presents results through a clean, interactive **Streamlit web app**
* Visualizes business insights through a **4-page Power BI Dashboard**

---

## 🚀 Live Demo

> Run locally by following the setup instructions below.

---

## 🗂️ Project Structure

```
customer-churn-pipeline/
│
├── churn_app.py              # Streamlit web application
├── churn_pipeline.py         # Model training and pipeline script
├── churn_predictions.csv     # Exported predictions for Power BI
├── churn_dashboard.pbix      # Power BI dashboard file
├── churn_dashboard.pdf       # Power BI dashboard exported as PDF
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── .gitignore                # Files excluded from version control
```

---

## 📊 Dataset

* **Source:** IBM Telco Customer Churn Dataset
* **Size:** 7,043 customers, 19 features
* **Target:** `Churn` — Yes (1) or No (0)
* **Class Distribution:** ~74% No Churn / ~26% Churn (imbalanced)

### Key Features Used

| Feature             | Description                              |
| ------------------- | ---------------------------------------- |
| `tenure`          | Number of months the customer has stayed |
| `Contract`        | Month-to-month, One year, Two year       |
| `MonthlyCharges`  | Monthly billing amount                   |
| `InternetService` | DSL, Fiber optic, or No                  |
| `OnlineSecurity`  | Whether the customer has online security |
| `TechSupport`     | Whether the customer has tech support    |
| `PaymentMethod`   | How the customer pays                    |

---

## 🧠 ML Pipeline

### Preprocessing

* **Numerical features** (`tenure`, `MonthlyCharges`, `TotalCharges`):
  * `SimpleImputer` (mean strategy)
  * `StandardScaler`
* **Categorical features** (all others):
  * `SimpleImputer` (most frequent strategy)
  * `OneHotEncoder` (handle_unknown="ignore")

### Model

* **Algorithm:** Random Forest Classifier
* **Class Imbalance Fix:** `class_weight="balanced"` to improve churn recall
* **Pipeline:** `ColumnTransformer` + `RandomForestClassifier` wrapped in `sklearn.Pipeline`

### Evaluation

| Metric           | Value                                |
| ---------------- | ------------------------------------ |
| Model Accuracy   | 78.50%                               |
| ROC-AUC Score    | ~0.83                                |
| Cross-validation | 5-fold CV                            |
| Churn Recall     | Improved with balanced class weights |

---

## 💻 App Features

* 📋 **Sidebar inputs** — all 19 customer attributes organized into sections
* 🔢 **Auto-calculated Total Charges** — derived from tenure × monthly charges
* 🎯 **Churn probability score** — not just a binary label
* 📊 **Visual risk bar** — progress bar showing churn risk level
* ⚠️ **Risk category** — High / Medium / Low risk with actionable messages
* 🛡️ **Error handling** — graceful message if model file is missing

---

## 📊 Power BI Dashboard

An interactive 4-page business dashboard built on top of the ML model predictions.

### Dashboard Pages

| Page                        | Description                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------ |
| 📄 Executive Summary        | KPI cards, churn by contract, risk distribution, churn by tenure                     |
| 📄 Customer Deep Dive       | Churn by internet service, payment method, gender, senior citizen, services impact   |
| 📄 Prediction Results       | Predicted vs actual churn, probability distribution, high risk table, model accuracy |
| 📄 Business Recommendations | Key findings, growth strategies, risk management, revenue impact                     |

### Key Dashboard Metrics

| Metric                  | Value   |
| ----------------------- | ------- |
| Total Customers         | 1,409   |
| Overall Churn Rate      | 26.5%   |
| High Risk Customers     | 104     |
| Monthly Revenue at Risk | $8,028  |
| Potential Annual Loss   | $96,336 |
| Model Accuracy          | 78.50%  |

### Risk Categories

| Risk Level     | Customers | Churn Probability |
| -------------- | --------- | ----------------- |
| 🔴 High Risk   | 104       | > 75%             |
| 🟡 Medium Risk | 221       | 45% — 75%        |
| 🟢 Low Risk    | 1,084     | < 45%             |

### How to Open the Dashboard

1. Download **Power BI Desktop** for free from [microsoft.com/power-bi](https://www.microsoft.com/power-bi)
2. Download `churn_dashboard.pbix` from this repo
3. Open the file in Power BI Desktop
4. All 4 pages load instantly with full interactivity

### Dashboard Files

* 📥 **Power BI file:** `churn_dashboard.pbix` — open in Power BI Desktop
* 📄 **PDF export:** `churn_dashboard.pdf` — view without Power BI

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/customer-churn-pipeline.git
cd customer-churn-pipeline
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Train the model (generates churn_pipeline.pkl and churn_predictions.csv)

```bash
python churn_pipeline.py
```

### 6. Run the Streamlit app

```bash
streamlit run churn_app.py
```

The app will open at `http://localhost:8501`

### 7. Open the Power BI Dashboard

```
Open churn_dashboard.pbix in Power BI Desktop
```

---

## 📦 Dependencies

```
streamlit==1.41.1
pandas==2.2.3
scikit-learn==1.5.1
numpy==2.0.1
matplotlib==3.9.2
seaborn==0.13.2
joblib==1.4.2
```

---

## 🔄 Version History

### Version 2.0 — Current (Improved)

* ✅ Replaced `pickle` with `joblib` for safer, faster model saving
* ✅ Added `class_weight="balanced"` to fix class imbalance
* ✅ Added ROC-AUC score and confusion matrix evaluation
* ✅ Added 5-fold cross-validation for reliable scoring
* ✅ Extracted feature importances from the trained model
* ✅ Moved app inputs to sidebar with grouped sections
* ✅ Auto-calculated TotalCharges (no manual input needed)
* ✅ Added churn probability score and visual risk bar
* ✅ Added High / Medium / Low risk category messages
* ✅ Added error handling for missing model file
* ✅ Fixed deprecated `inplace=True` pandas syntax
* ✅ Built 4-page Power BI business dashboard

### Version 1.0 — Basic (1 year ago)

* Binary churn prediction only
* No class imbalance handling
* Single train/test split evaluation
* All inputs in main panel
* No error handling
* No business dashboard

---

## 📈 Key Business Insights

Based on the trained model and Power BI analysis, the top factors that drive churn are:

1. **Contract type** — Month-to-month customers churn significantly more
2. **Tenure** — Newer customers (0-20 months) are at much higher risk
3. **Internet Service** — Fiber optic customers have surprisingly high churn
4. **Monthly Charges** — Higher charges correlate with higher churn
5. **Online Security & Tech Support** — Absence of these services increases churn risk
6. **Payment Method** — Electronic check users churn the most
7. **Senior Citizens** — Churn 26% more than non-senior customers

---

## 🎯 Business Value

| Use Case                                         | Impact                                               |
| ------------------------------------------------ | ---------------------------------------------------- |
| Identify high-risk customers early               | Enables proactive retention campaigns                |
| Prioritize customers above 75% churn probability | Efficient use of retention budget                    |
| Contract type insights                           | Push annual/two-year contracts over monthly          |
| No-code UI for business users                    | Retention teams can use it without data expertise    |
| Power BI dashboard for management                | Executive level insights without technical knowledge |
| Revenue at risk tracking                         | $96,336 potential annual loss identified             |

---

## ✅ What TO DO — Growth Strategies

1. **Push Annual Contracts** — Offer discounts to switch month-to-month customers
2. **Bundle Tech Support & Security** — Customers with Tech Support churn 26% less
3. **Target High Risk Customers Early** — Contact 104 High Risk customers immediately
4. **Reward Loyal Customers** — Create loyalty rewards for 60+ month customers
5. **Improve Fiber Optic Value** — Improve service quality or offer price relief
6. **Promote Auto Payment Methods** — Incentivize switch from electronic check
7. **Senior Citizen Special Plans** — Create affordable dedicated plans

---

## ❌ What NOT TO DO — Risk Management

1. **Don't ignore month-to-month customers** — Highest churn risk group
2. **Don't offer Fiber Optic without support services** — Dramatically increases churn
3. **Don't neglect new customers** — First 20 months are critical
4. **Don't rely on electronic check payments** — Highest churn payment method
5. **Don't treat all customers the same** — Different groups need different strategies
6. **Don't wait for customers to complain** — Use model proactively

---

## 🔮 Future Improvements

* [ ] Add SHAP explainability — show *why* a customer is predicted to churn
* [ ] Hyperparameter tuning with GridSearchCV
* [ ] Model comparison — Logistic Regression vs XGBoost vs Random Forest
* [ ] Connect to live customer database
* [ ] Deploy on Streamlit Cloud or AWS
* [ ] Add model performance monitoring and data drift detection
* [ ] Publish Power BI dashboard online with Pro license

---

## 👤 Author

**Your Name  Dipali Chothmal**

* LinkedIn: https://www.linkedin.com/in/dipali-chothmal-5731b032b/
* GitHub: https://github.com/Dipali-cpu

---

## 📄 License

This project is open source and available under the [MIT License](https://claude.ai/chat/LICENSE).
