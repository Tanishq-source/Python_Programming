import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*50

###############################################################
# Step 1 : Load the Dataset
###############################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DatasetPath = "iris.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully...")
print("Initial entries from dataset :")
print(df.head())

###############################################################
# Step 2 : Data Analysis (EDA)
###############################################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of dataset : ",df.shape)
print("Column Names : ",list(df.columns))

print("Missing values (Per Column)")
print(df.isnull().sum())

print("Class Distribution (species count)")
print(df["species"].value_counts())

print("Statistical Report of Dataset")
print(df.describe())

###############################################################
# Step 3 : Decide Independent and Dependent Variables
###############################################################

print(Border)
print("Step 3 : Decide Independent and Dependent Variables")
print(Border)

# X : Independent Variables / Features 
# Y : Dependent Variables / Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[feature_cols]
Y = df["species"]

print("X shape :",X.shape)
print("Y shape :",Y.shape)

###############################################################
# Step 4 : Visualization of Dataset
###############################################################

print(Border)
print("Step 4 : Visualization of Dataset")
print(Border)

# Scatter plot 
plt .figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label = sp)

plt.title("Iris : Petal Length vs Petal width")
plt.xlabel("petal length (cm)")    
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid(True)
plt.show() 

###############################################################
# Step 5 : Split the Dataset for training and testing
###############################################################

print(Border)
print("Step 5 : Split the Dataset for training and testing")
print(Border)

# Test Size = 20%
# Train Size = 80%

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

print("Data splitting activity done : ")

print("X - Independent : ",X.shape)   # (150,4)
print("Y - Dependent : ",Y.shape)     # (150,)

print("X_train : ",X_train.shape)     # (120,4)
print("X_test : ",X_test.shape)       # (30,4)

print("Y_train : ",Y_train.shape)     # (120,)
print("Y_test : ",Y_test.shape)       # (30,)

