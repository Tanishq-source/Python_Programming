import psutil
import sys 
import os
import time
import schedule

def CreateLog(FolderName):
     Border = "-"*50

     Ret = False

     Ret = os.path.exists(FolderName)

     if(Ret == True):
          Ret = os.path.isdir(FolderName)
          if(Ret == False):
               print("Unable to create folder")
               return

     else:
        os.mkdir(FolderName)
        print("Directory for Log files gets created successfully")

     timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
     FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
     print("Log file gets created with name : ",FileName)  

     fobj = open(FileName,"w")

     fobj.write(Border+"\n")
     fobj.write("-----Marvellous platform surveillance system------\n")
     fobj.write("Log created at : "+time.ctime()+"\n")
     fobj.write(Border+"\n\n")

     fobj.write("------------------------System Report------------------------\n")

     # print("CPU Usage : ",psutil.cpu_percent())
     fobj.write("CPU Usage :%s %%\n" %psutil.cpu_percent())
     fobj.write(Border+"\n")

     fobj.write("\nDisk Usage Report\n")

     mem = psutil.virtual_memory()
     # print("RAM Usage : ",mem.percent)
     fobj.write("RAM Usage : %s %%\n" %mem.percent)
     fobj.write(Border+"\n")

     for part in psutil.disk_partitions():
          try:
            usage = psutil.disk_usage(part.mountpoint)
            # print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s %% used\n" %(part.mountpoint,usage.percent))
          except:
              pass

     fobj.write(Border+"\n")      

     net = psutil.net_io_counters()
     fobj.write("\nNetwork Usage Report\n")
     fobj.write("Sent : %.2f MB\n" %(net.bytes_sent / (1024 * 1024)))
     fobj.write("Recv : %.2f MB\n" %(net.bytes_recv / (1024 * 1024)))
     fobj.write(Border+"\n")
     
     # Process Log

     fobj.write(Border+"\n")
     fobj.write("-------------End of Log file-------------\n")
     fobj.write(Border+"\n")

      

def main():
    Border = "-"*50
    print(Border)
    print("-----Marvellous platform surveillance system------")
    print(Border)

    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to :")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends mail with log")
            print("4 : Store information about processor")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM")
            print("7 : Store information about secondary storage")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("USe the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")    
            
        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # python Demo.py 5 Marvellous
    elif(len(sys.argv) == 3):
        print("Inside Project's logic")
        print("TimeInterval : ",sys.argv[1])
        print("DirectoryName : ",sys.argv[2])
        
        # Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])

        print("Platform surveillance system started successfully")
        print("Directory created with name : ",sys.argv[2])
        print("Time Interval in minutes : ",sys.argv[1])
        print("Press ctrl + c to stop the execution")

        # wait till abort
        while(True):
             schedule.run_pending()
             time.sleep(1)

    else:
            print("Invalid number of command line arugements")
            print("Unable to proceed as tere is no such option")
            print("Please use --h or --u to get more details")    


    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)

if __name__ == "__main__":
    main()  