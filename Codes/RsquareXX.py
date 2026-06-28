from sklearn.metrics import r2_score

def main():
    Y_actual = [3,4,2,4,5]                  # Y
    Y_predicted = [3,4,2,4,5]               # Yp

    r2 = r2_score(Y_actual,Y_predicted)

    print("Actual Values : Y ",Y_actual)
    print("Predicted Values : Yp ",Y_predicted)
    print("R square value : ",r2)                   # 0.307



if __name__ == "__main__":
    main()   