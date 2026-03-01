# Functional

# def CheckEven(No):
    #return (No % 2 == 0)

CheckEven = lambda No : (No % 2 == 0) 

def main():
    Value = 0
    Ret = False

    print("Enter Number :")
    Value = int(input())

    Ret = CheckEven(Value)

    if(Ret == True):
        print("Number is Even")
    else:
        print("Number is Odd")       

if __name__ == "__main__":
    main()    