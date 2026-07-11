import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load datasets
app = pd.read_csv("dataset/application_record.csv")
credit = pd.read_csv("dataset/credit_record.csv")

# Convert STATUS into binary
def to_binary(status):
    if status in ['0', 'X', 'C']:
        return 1
    else:
        return 0

credit["STATUS_BIN"] = credit["STATUS"].apply(to_binary)

# Merge datasets
df = app.merge(credit, how="left", on="ID")

# Fill missing values
df["STATUS_BIN"] = df["STATUS_BIN"].fillna(0)
df["OCCUPATION_TYPE"] = df["OCCUPATION_TYPE"].fillna("Unknown")

# Label Encode all categorical columns
encoder = LabelEncoder()

categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    df[column] = encoder.fit_transform(df[column].astype(str))

print("Categorical columns encoded successfully!")

print("\nEncoded Dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)