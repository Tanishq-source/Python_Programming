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
#   Function name : CleanTitanicData
#   Description :   It does preprocessing
#                   It removes unnecessary columns
#                   It hanles missing values
#                   It converts text data to numeric format
#                   It does encoding to categorical columns
#   Parameters :    df -> pandas dataframe       
#   Return :        df -> Clean pandas dataframe 
#   Date :          14/03/26
#   Autor :         Tanishq Nitin Chandole
#---------------------------------------------------------------

def CleanTitanicData(df):    
    DisplayInfo("Step 2 : Original Data")
    print(df.head())

    # Remove unecessary columns
    drop_columns = ["Passengerid","zero","Name","Cabin"]
    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\nColumns to be droped : ")
    print(existing_columns)

    # Drop the unwanted columns
    df = df.drop(columns = existing_columns)
    DisplayInfo("Step 2 : Data after column removal")
    print(df.head())

    # Handle age column
    if "Age" in df.columns:
        print("Age column before filling missing values")
        print(df["Age"].head(10))   

        # coerce = Invalid value gets converted as NaN
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

        age_median = df["Age"].median()

        # Replace missing values with median    
        df["Age"] = df["Age"].fillna(age_median)

        print("Age column after preprocessing : ")
        print(df["Age"].head(10))

    # Handle fare column
    if "Fare" in df.columns:
        print("\nFare column before preprocessing")
        print(df["Fare"].head(10))

        df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")    

        fare_median = df["Fare"].median()

        print("\nMedian of fare column is : ",fare_median)

        # Replace missing values with median    
        df["Fare"] = df["Fare"].fillna(fare_median)

        print("\nFare column after preprocessing")
        print(df["Fare"].head(10))

    # Handle Embarked column
    if "Embarked" in df.columns:
        print("\nEmbarked column before preprocessing")
        print(df["Embarked"].head(10))

        # Convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        # Reove missing values
        df["Embarked"] = df["Embarked"].replace(('nan','None',''),np.nan)

        # Get most frequent value
        embarked_mode = df["Embarked"].mode()[0]
        print("Mode of embarked column : ",embarked_mode)

        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("\nEmbarked column after preprocessing")
        print(df["Embarked"].head(10))

    # Handle Sex column
    if "Sex" in df.columns:
        print("\nSex column before preprocessing")
        print(df["Sex"].head(10))

        df["Sex"] = pd.to_numeric(df["Sex"], errors="coerce")    

        print("\nSex column after preprocessing")
        print(df["Sex"].head(10))

    DisplayInfo("Data after preprocessing")
    print(df.head())

    print("\nMissing values after preprocessing")
    print(df.isnull().sum())            

    return df

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

    df = CleanTitanicData(df) 

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