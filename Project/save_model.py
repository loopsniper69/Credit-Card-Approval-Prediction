import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load datasets
app = pd.read_csv("dataset/application_record.csv")
credit = pd.read_csv("dataset/credit_record.csv")

# Convert STATUS to binary
def convert_status(status):
    if status in ['0', 'C', 'X']:
        return 1
    return 0

credit["STATUS_BIN"] = credit["STATUS"].apply(convert_status)

# Aggregate one record per applicant
credit = credit.groupby("ID").agg({
    "STATUS_BIN": "max",
    "MONTHS_BALANCE": "max"
}).reset_index()

# Merge
df = app.merge(credit, on="ID", how="left")

# Fill missing values
df["STATUS_BIN"] = df["STATUS_BIN"].fillna(0)
df["MONTHS_BALANCE"] = df["MONTHS_BALANCE"].fillna(0)
df["OCCUPATION_TYPE"] = df["OCCUPATION_TYPE"].fillna("Unknown")
df = df.fillna(0)

# Encode categorical columns
encoder = LabelEncoder()

for col in df.select_dtypes(include=["object"]).columns:
    df[col] = encoder.fit_transform(df[col].astype(str))

# Features and target
features = [
    "CODE_GENDER",
    "AMT_INCOME_TOTAL",
    "NAME_INCOME_TYPE",
    "NAME_EDUCATION_TYPE",
    "FLAG_OWN_REALTY"
]

X = df[features]
y = df["STATUS_BIN"]

# Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved successfully as model.pkl")