import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousAdvertise(Datapath):
    Border = "-"*50

    #--------------------------------------------------
    # Step 1 : Load Dataset
    #--------------------------------------------------
    print(Border)
    print("Step 1 : Load Dataset")
    print(Border)

    df = pd.read_csv(Datapath)

    print("Few records from the dataset : ")
    print(df.head())

    #--------------------------------------------------
    # Step 2 : Remove Unwanted Columns
    #--------------------------------------------------
    print(Border)
    print("Step 2 : Remove Unwanted Columns")
    print(Border)

    print("Shape of dataset before removal : ",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Shape of dataset after removal : ",df.shape)    

    print(Border)
    print("Clean Dataset is : ")
    print(Border)

    print(df.head())

    #--------------------------------------------------
    # Step 3 : Check missing values
    #--------------------------------------------------
    print(Border)
    print("Step 3 : Check missing values")
    print(Border)

    print("Missing values count : \n",df.isnull().sum())

    #--------------------------------------------------
    # Step 4 : Display Statistical summary
    #--------------------------------------------------
    print(Border)
    print("Step 4 : Display Statistical summary")
    print(Border)

    print(df.describe())

    #--------------------------------------------------
    # Step 5 : Correlation between columns
    #--------------------------------------------------
    print(Border)
    print("Step 5 : Correlation between columns")
    print(Border)

    print("Correlation matrix")
    print(df.corr())

    #--------------------------------------------------
    # Step 6 : Split Dataset into Independent and Dependent Variables
    #--------------------------------------------------
    print(Border)
    print("Step 6 : Split Dataset into Independent and Dependent Variables")
    print(Border)

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape of Independent Variables : ",X.shape)
    print("Shape of Dependent Variables : ",Y.shape)

    #--------------------------------------------------
    # Step 7 : Split Dataset for Training and Testing
    #--------------------------------------------------
    print(Border)
    print("Step 7 : Split Dataset for Training and Testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train Shape : ",X_train.shape)
    print("X_test Shape : ",X_test.shape)
    print("Y_train Shape : ",Y_train.shape)
    print("Y_test Shape : ",Y_test.shape)

    #--------------------------------------------------
    # Step 8 : Create and train the model 
    #--------------------------------------------------
    print(Border)
    print("Step 8 : Create the model")
    print(Border)

    model = LinearRegression()
    model.fit(X_train,Y_train)

    #--------------------------------------------------
    # Step 9 : Test the model 
    #--------------------------------------------------
    print(Border)
    print("Step 9 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test)

    #--------------------------------------------------
    # Step 10 : Evaluate the model 
    #--------------------------------------------------
    print(Border)
    print("Step 10 : Evaluate the model")
    print(Border)
    
    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)

    print("Mean Squared Error : ",MSE)
    print("Root Mean Squared Error : ",RMSE)
    print("R Sqaure value : ",R2)

    #--------------------------------------------------
    # Step 11 : Calculate Model Coefficient 
    #--------------------------------------------------
    print(Border)
    print("Step 11 : Calculate Model Coefficient")
    print(Border)

    for column, value in zip(X.columns,model.coef_):
        print(f"{column} : {value}")

    print("Intercept : ",model.intercept_) 

    #--------------------------------------------------
    # Step 12 : Compare the Actual and Predicted values
    #--------------------------------------------------
    print(Border)
    print("Step 12 : Compare the Actual and Predicted values")
    print(Border)   

    Result = pd.DataFrame({'Actual sale' : Y_test.values,
                           'Predicted sale' : Y_pred
                          })
    print(Result.head())

    #--------------------------------------------------
    # Step 13 : Plot Actual vs Predicted
    #--------------------------------------------------
    print(Border)
    print("Step 13 : Plot Actual vs Predicted")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.scatter(Y_test,Y_pred)
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales")
    plt.title("Actual sales vs Predicted sales")
    plt.grid(True)
    plt.show()

def main():
    MarvellousAdvertise("Advertising.csv")
    
if __name__ == "__main__":
    main()    