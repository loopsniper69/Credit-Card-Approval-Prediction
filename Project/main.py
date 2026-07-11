import pandas as pd

app = pd.read_csv("dataset/application_record.csv")
credit = pd.read_csv("dataset/credit_record.csv")

print("========== MISSING VALUES ==========")
print(app.isnull().sum())

print("\n========== DUPLICATE RECORDS ==========")
print(app.duplicated().sum())

print("\n========== CREDIT DATASET MISSING VALUES ==========")
print(credit.isnull().sum())

print("\n========== CREDIT DATASET DUPLICATES ==========")
print(credit.duplicated().sum())