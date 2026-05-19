import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline
try:
    model = joblib.load("churn_pipeline.pkl")
except FileNotFoundError:
    st.error("Model file not found. Please ensure churn_pipeline.pkl is in the same folder.")
    st.stop()

# Page title
st.title("🔮 Customer Churn Prediction App")
st.write("Enter customer details to predict if they will churn.")

# Sidebar input fields
with st.sidebar:
    st.header("Customer Details")

    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col2:
        senior = st.selectbox("Senior Citizen", ["No", "Yes"])

    col3, col4 = st.columns(2)
    with col3:
        partner = st.selectbox("Has Partner?", ["Yes", "No"])
    with col4:
        dependents = st.selectbox("Has Dependents?", ["Yes", "No"])

    tenure = st.number_input("Tenure (in months)", min_value=0, max_value=72, value=12)

    st.subheader("Services")
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

    st.subheader("Billing")
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=70.0)
    total_charges = monthly_charges * tenure

    st.info(f"Auto-calculated Total Charges: **${total_charges:.2f}**")

# Main panel — prediction
st.markdown("---")
if st.button("Predict Churn", use_container_width=True):

    input_data = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])

    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"### 🔴 This customer is likely to Churn")
    else:
        st.success(f"### 🟢 This customer is likely to Stay")

    st.metric(label="Churn Probability", value=f"{proba:.1%}")
    st.progress(float(proba), text="Churn Risk Level")

    # Risk category
    if proba >= 0.75:
        st.warning("⚠️ High Risk — Immediate retention action recommended.")
    elif proba >= 0.45:
        st.warning("🟡 Medium Risk — Monitor this customer closely.")
    else:
        st.info("✅ Low Risk — Customer appears stable.")