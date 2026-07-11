import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
app = pd.read_csv("dataset/application_record.csv")

# Graph size
plt.figure(figsize=(15,6))

# Count occupation types
print(app["OCCUPATION_TYPE"].value_counts())

# Plot
sns.countplot(
    x="OCCUPATION_TYPE",
    data=app,
    order=app["OCCUPATION_TYPE"].value_counts().index
)

plt.xticks(rotation=90)
plt.title("Occupation Type Distribution")
plt.tight_layout()
plt.show()