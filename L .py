import pandas as pd

# Load data from common formats
df = pd.read_csv("data.csv")
# df = pd.read_excel("data.xlsx")
# df = pd.read_json("data.json")

# Quick inspection
print(df.head(5))  # First 5 rows
print(df.info())  # Column types & missing values
print(df.describe())  # Summary statistics (mean, std, min, max)
