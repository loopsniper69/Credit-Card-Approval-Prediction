import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
app = pd.read_csv("dataset/application_record.csv")

# Select only numeric columns
numeric_data = app.select_dtypes(include=["int64", "float64"])

# Correlation matrix
corr = numeric_data.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()