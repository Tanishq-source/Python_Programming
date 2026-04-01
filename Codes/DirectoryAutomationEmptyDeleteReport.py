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
    
    FileCount = 0   
    EmptyFileCount = 0
    
    for FolderName,SubFolder,FileName in os.walk(DirName):
        for fname in FileName:
            FileCount = FileCount + 1

            fname = os.path.join(FolderName,fname)
            print("File Name : ",fname)
            print("File Size : ",os.path.getsize(fname))     

            if(os.path.getsize(fname) == 0):                # Empty File
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)

    Border = "-"*50
    print(Border)
    print("--------------- Automation report ----------------")
    print("Total files scanned : ",FileCount)
    print("Total empty files found : ",EmptyFileCount)
    print(Border)     

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

    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

if __name__ == "__main__":
    main()    