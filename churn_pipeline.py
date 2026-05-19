import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

# Load & clean
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df.drop("customerID", axis=1, inplace=True)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].mean())

X = df.drop("Churn", axis=1)
y = df["Churn"].map({"Yes": 1, "No": 0})

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Preprocessing
numeric_features = ["tenure", "MonthlyCharges", "TotalCharges"]
categorical_features = [c for c in X.columns if c not in numeric_features]

preprocessor = ColumnTransformer([
    ("num", Pipeline([
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ]), numeric_features),
    ("cat", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ]), categorical_features)
])

clf_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced"   # fixes class imbalance
    ))
])

# Train & evaluate
clf_pipeline.fit(X_train, y_train)
y_pred = clf_pipeline.predict(X_test)
y_proba = clf_pipeline.predict_proba(X_test)[:, 1]

print(classification_report(y_test, y_pred))
print(f"ROC-AUC: {roc_auc_score(y_test, y_proba):.4f}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")

# Cross-validation
cv_scores = cross_val_score(clf_pipeline, X, y, cv=5, scoring="roc_auc")
print(f"CV ROC-AUC: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

# Save
joblib.dump(clf_pipeline, "churn_pipeline.pkl")
print("Model saved successfully.")


# Export predictions for Power BI
X_test_copy = X_test.copy()
X_test_copy["Actual_Churn"] = y_test.values
X_test_copy["Predicted_Churn"] = y_pred
X_test_copy["Churn_Probability"] = y_proba
X_test_copy["Risk_Category"] = pd.cut(
    X_test_copy["Churn_Probability"],
    bins=[-0.01, 0.45, 0.75, 1.0],
    labels=["Low Risk", "Medium Risk", "High Risk"]
)


X_test_copy.to_csv("churn_predictions.csv", index=False)
print("churn_predictions.csv exported successfully!")