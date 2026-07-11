import pandas as pd

# Load datasets
app = pd.read_csv("dataset/application_record.csv")
credit = pd.read_csv("dataset/credit_record.csv")

print("Application Shape:", app.shape)
print("Credit Shape:", credit.shape)

# ----------------------------
# Convert STATUS to Binary
# ----------------------------

def to_binary(status):
    if status in ['0', 'X', 'C']:
        return 1
    else:
        return 0

credit["STATUS_BIN"] = credit["STATUS"].apply(to_binary)

print("\nBinary Status Count:")
print(credit["STATUS_BIN"].value_counts())

# ----------------------------
# Merge both datasets
# ----------------------------

final_df = app.merge(credit, how="left", on="ID")

print("\nMerged Dataset Shape:", final_df.shape)

print("\nFirst Five Rows")
print(final_df.head())

print("\nMissing Values")
print(final_df.isnull().sum().sort_values(ascending=False))