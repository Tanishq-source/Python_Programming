import numpy as np
import pandas as pd
import matplotlib as plt

def MarvellousPredictor():
    # Load the Data 
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent Variables : X - ",X)
    print("Values of Dependent Variables : Y - ",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("X_MEAN is : ",mean_x)
    print("Y_MEAN is : ",mean_y)

    n = len(X)  # 5

    # Y = mX + C

    # m = (summ (x - X_bar) * (y - Y_bar)) / (summ (x - X_bar) ** 2)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator

    print("Slope of line ie m : ",m)      # 0.4

    C = mean_y - (m * mean_x)

    print("Y intercept of line ie C : ",C)

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()    