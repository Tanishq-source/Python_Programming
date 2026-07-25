import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error,r2_score

#------------------------------------------------------------
# Step 1 : Load the Dataset
#------------------------------------------------------------

df = pd.read_csv("california_housing.csv")

print("Shape of dataset : ",df.shape)
print("First 5 records : ",df.head())

#------------------------------------------------------------
# Step 2 : Separate Features and Labels
#------------------------------------------------------------    

X = df.drop("target",axis=1)
Y = df["target"]

#------------------------------------------------------------
#  Step 3 : Split Dataset for Training and Testing
#------------------------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#------------------------------------------------------------
#  Step 4 : Create Base Model 
#------------------------------------------------------------

model = DecisionTreeRegressor(random_state=42)
    
#------------------------------------------------------------
#  Step 5 : Train Bagging Model
#------------------------------------------------------------

model.fit(X_train,Y_train)

#------------------------------------------------------------
#  Step 6 : Test Bagging Model
#------------------------------------------------------------

Y_pred = model.predict(X_test)  

#------------------------------------------------------------
#  Step 7 : Evaluate Bagging Model
#------------------------------------------------------------

print("MeanSquaredError : ",mean_squared_error(Y_test,Y_pred))

print("R Square : ",r2_score(Y_test,Y_pred))    