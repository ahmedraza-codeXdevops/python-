# Select specific columns
columns = df[["Name", "Age", "Salary"]]

# Filter rows by condition
high_earners = df[df["Salary"] > 70000]

# Multiple conditions (& for AND, | for OR)
filtered = df[(df["Age"] >= 25) & (df["Department"] == "Engineering")]

# Select by index/position (.iloc) or label (.loc)
subset = df.iloc[0:10, 0:3]  # First 10 rows, first 3 columns
