import sys
import os

def DirectoryScanner(DirName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("Their is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName,SubFolder,FileName in os.walk(DirName):
        for fname in FileName:
            print("File Name : ",fname)
            print("File Size : ",os.path.getsize(fname))     # Path issue  

def main(): 
    Border = "-"*50
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify te name of Directory")
        return
    
    DirectoryScanner(sys.argv[1])

if __name__ == "__main__":
    main()    