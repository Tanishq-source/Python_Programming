def main():
    try:
        open("Hello.txt","w")
        print("File gets successfully opened")

    except FileNotFoundError:
        print("Unable to open file as their is no such file")

    finally:
        print("End of application")     

if __name__ == "__main__":
    main()
