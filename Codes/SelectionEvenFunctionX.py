# Procedural

def CheckEven(No):
    if(No % 2 == 0):
        print("Number is even")
    else:
        print("Number is odd")  

def main():
    Value = 0

    print("Enter Number :")
    Value = int(input())

    CheckEven(Value)

if __name__ == "__main__":
    main()    