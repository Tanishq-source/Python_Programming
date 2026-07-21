import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    #-------------------------------------------------------------
    # Step 1 : Load the Dataset
    #-------------------------------------------------------------
    print("Step 1 : Load the Dataset")
    df = pd.read_csv("Mall_Customers.csv")

    print("First few Records :")
    print(df.head())

    print("Shape of Dataset")
    print(df.shape)

    print("Missing values")
    print(df.isnull().sum())  

    #-------------------------------------------------------------
    # Step 2 : Select Features (Independent)
    #-------------------------------------------------------------  

    X = df[["AnnualIncome","SpendingScore"]]
    print("Selected Features : ")   
    print(X.head())     

if __name__ == "__main__":
    main()
