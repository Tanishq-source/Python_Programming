#  [A,B,C,D]
# X[1,2,3,5]
# Y[2,3,1,6]
#  [R,R,B,B]

# Predict(3,3) -> ?

import numpy as np
import math

def EuclideanDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)

    return Ans

def MarvellousKNeighborsClassifier():
    border = "-"*50

    data = [
                {'point' : 'A','X' : 1,'Y' : 2,'Label' : 'Red'},
                {'point' : 'B','X' : 2,'Y' : 3,'Label' : 'Red'},
                {'point' : 'C','X' : 3,'Y' : 1,'Label' : 'Blue'},
                {'point' : 'D','X' : 5,'Y' : 6,'Label' : 'Blue'}
           ]
    
    print(border)
    print("Marvellous UserDefined KNN")
    print(border)

    print(border)
    print("Training Dataset")
    print(border)

    for i in data:
        print(i)

    print(border)  

    new_points = {'X' : 3,'Y' : 3}

   # Calculate all Distances 
    for d in data:
        d['distance'] = EuclideanDistance(d,new_points)

    print(border)
    print("Calculated distances are : ")
    print(border)

    for d in data:
        print(d)   

    sorted_data = sorted(data,key=lambda item : item['distance'])   

    print(border)
    print("Sorted Data is : ")
    print(border)

    for d in sorted_data:
        print(d)   

    K = 3
    nearest = sorted_data[:K]

    print(border)
    print("Nearest 3 elements are : ")
    print(border)

    for d in nearest:
        print(d)   

    # Voting
    Votes = {}
    
    for neighbour in nearest:
        Label = neighbour['Label']
        Votes[Label] = Votes.get(Label,0) + 1

    print(border)
    print("Voting Result is : ")
    print(border)

    for d in Votes:
        print("Name : ",d,"Value : ",Votes[d])  

    print(border)  

    Predicted_class = max(Votes,key=Votes.get)

    print("Predicted Class of (3,3) is : ",Predicted_class)        

def main():
    MarvellousKNeighborsClassifier()

if __name__ == "__main__":
    main()    