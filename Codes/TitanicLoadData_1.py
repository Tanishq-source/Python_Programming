import pandas as pd
import numpy as np
import joblib as jb

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix 

#---------------------------------------------------------------
#   Function name : DisplayInfo
#   Description :   It displays the formated title 
#   Parameters :    title (str)
#   Return :        None
#   Date :          14/03/26
#   Autor :         Tanishq Nitin Chandole
#---------------------------------------------------------------

def DisplayInfo(title):
    print("\n" + "="*70)
    print(title)
    print("="*70)

#---------------------------------------------------------------
#   Function name : ShowData
#   Description :   It shows basic information about dataset
#   Parameters :    df
#                   df ->   Pandas dataframe object
#                   Messsage
#                   Message ->  Heading text to display
#   Return :        None
#   Date :          14/03/26
#   Autor :         Tanishq Nitin Chandole
#---------------------------------------------------------------

def ShowData(df,message):    
    DisplayInfo(message)

    print("\nFirst 5 rows of dataset")
    print(df.head())

    print("\nShape of dataset")
    print(df.shape) 

    print("\nColumn names : ")
    print(df.columns.tolist())

    print("\nMissing values of each columns")
    print(df.isnull().sum())

#---------------------------------------------------------------
#   Function name : MarvellousTitanicLogistics
#   Description :   This is main pipeline controller
#                   It loads the dataset,shows the raw data
#                   It Preprocess te dataset & train the model 
#   Parameters :    Datapath of dataset file
#   Return :        None
#   Date :          14/03/26
#   Autor :         Tanishq Nitin Chandole
#---------------------------------------------------------------

def MarvellousTitanicLogistics(Datapath):
    DisplayInfo("Step 1 : Loading the Dataset")

    df = pd.read_csv(Datapath)    

    ShowData(df,"Initial Dataset")  

#---------------------------------------------------------------
#   Function name : main
#   Description :   Strating point of te application
#   Parameters :    None
#   Return :        None
#   Date :          14/03/26
#   Autor :         Tanishq Nitin Chandole
#---------------------------------------------------------------

def main():
    MarvellousTitanicLogistics("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()    