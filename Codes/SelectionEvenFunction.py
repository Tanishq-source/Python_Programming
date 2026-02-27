def CheckEven(No):
    if(No % 2 == 0):
        print("Number is even")
    else:
        print("Number is odd")  

def main():
    CheckEven(21)           # Positional
    CheckEven(No = 22)      # Keyword

if __name__ == "__main__":
    main()    