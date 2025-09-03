# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load dataset safely
try:
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to DataFrame
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print("An error occurred while loading the dataset:", str(e))

# Display first few rows
print("\nFirst 5 rows of dataset:")
print(df.head())

# Explore structure
print("\nData Info:")
print(df.info())

# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Clean dataset (no missing values in Iris, but example shown)
df = df.dropna()   # Or df.fillna(value, inplace=True)

# Task 2: Basic Data Analysis
print("\nBasic statistics:")
print(df.describe())

# Group by species and compute mean of numerical columns
grouped = df.groupby("target").mean()
print("\nMean values grouped by species:")
print(grouped)

# Map target numbers to species names
df["species"] = df["target"].map(dict(zip(range(3), iris.target_names)))

print("\nInteresting Finding:")
print("On average, Virginica species have the largest petal length and width, "
      "while Setosa species have the smallest.")

# Task 3: Data Visualization
plt.style.use("seaborn-v0_8")

# 1. Line chart (trend of sepal length across samples, just as an example of 'time series')
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart - Sepal Length over Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(6,4))
sns.barplot(x="species", y="petal length (cm)", data=df, estimator="mean", ci=None)
plt.title("Bar Chart - Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Avg Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(6,4))
plt.hist(df["sepal width (cm)"], bins=15, edgecolor="black")
plt.title("Histogram - Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (sepal length vs petal length, colored by species)
plt.figure(figsize=(7,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)",
                hue="species", data=df, palette="Set1")
plt.title("Scatter Plot - Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
