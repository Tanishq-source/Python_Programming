import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

def MarvellousClassifier(Datapath):
    Border = "-"*50

    # Step 1 : Load the Dataset from CSV file
    print(Border)
    print("Step 1 : Load the Dataset from CSV file")
    print(Border)

    df = pd.read_csv(Datapath)
    print("Some entries from dataset")
    print(df.head())
    print(Border)

    # Step 2 : Clean te dataset by removing empty rows
    print(Border)
    print("Step 2 : Clean te dataset by removing empty rows")
    print(Border)

    df.dropna(inplace = True)
    print("Total records : ",df.shape[0])
    print("Total columns : ",df.shape[1])
    print(Border)

    # Step 3 : Separate Independent and Dependent Variables
    print(Border)
    print("Step 3 : Separate Independent and Dependent Variables")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Border)
    print("Input columns : ",X.columns.to_list())
    print("Output column : Class")

def main():
    Border = "-"*50

    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()    