import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# =====================================================
# Load Datasets
# =====================================================

app = pd.read_csv("dataset/application_record.csv")
credit = pd.read_csv("dataset/credit_record.csv")

# =====================================================
# Convert Credit Status into Binary
# Good Customer = 1
# Bad Customer = 0
# =====================================================

def convert_status(status):
    if status in ['0', 'C', 'X']:
        return 1
    else:
        return 0

credit["STATUS_BIN"] = credit["STATUS"].apply(convert_status)

# =====================================================
# Create ONE record per customer
# =====================================================

credit = credit.groupby("ID").agg({
    "STATUS_BIN": "max",
    "MONTHS_BALANCE": "max"
}).reset_index()

# =====================================================
# Merge
# =====================================================

df = app.merge(credit, on="ID", how="left")

# =====================================================
# Fill Missing Values
# =====================================================

df["STATUS_BIN"] = df["STATUS_BIN"].fillna(0)
df["MONTHS_BALANCE"] = df["MONTHS_BALANCE"].fillna(0)
df["OCCUPATION_TYPE"] = df["OCCUPATION_TYPE"].fillna("Unknown")

# Fill any remaining missing values
df = df.fillna(0)

# =====================================================
# Encode Categorical Columns
# =====================================================

encoder = LabelEncoder()

categorical_columns = df.select_dtypes(include=["object"]).columns

for column in categorical_columns:
    df[column] = encoder.fit_transform(df[column].astype(str))

# =====================================================
# Features and Target
# =====================================================

X = df.drop(["STATUS_BIN"], axis=1)
y = df["STATUS_BIN"]

# =====================================================
# Train Test Split
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================================
# Logistic Regression
# =====================================================

lr = LogisticRegression(max_iter=1000)

lr.fit(X_train, y_train)

pred_lr = lr.predict(X_test)

print("=" * 50)
print("Logistic Regression Accuracy")
print(accuracy_score(y_test, pred_lr))

# =====================================================
# Decision Tree
# =====================================================

dt = DecisionTreeClassifier(random_state=42)

dt.fit(X_train, y_train)

pred_dt = dt.predict(X_test)

print("=" * 50)
print("Decision Tree Accuracy")
print(accuracy_score(y_test, pred_dt))

# =====================================================
# Random Forest
# =====================================================

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

pred_rf = rf.predict(X_test)

print("=" * 50)
print("Random Forest Accuracy")
print(accuracy_score(y_test, pred_rf))

print("=" * 50)
print("Model Training Completed Successfully")