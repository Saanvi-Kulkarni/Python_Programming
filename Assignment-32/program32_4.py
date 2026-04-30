import os
import sys
import time
import FileUtils

def main():
    Border = "-"*50
    print(Border)
    print("----------------- Directory Log ------------------")
    print(Border)

    if (len(sys.argv) != 2):
        print("Invalid number of arguments") 
        return   
    
    DirName = sys.argv[1]

    fobj = open("DirectoryLog3.txt", "w")
    fobj.write(Border + "\n")
    fobj.write("This is a log file\n")
    fobj.write(Border + "\n")

    StartTime = time.time()

    FileUtils.DirectoryDuplicateRemover(DirName, fobj)

    EndTime = time.time()
    ExecutionTime = EndTime - StartTime
    fobj.write("Execution time : " +str(ExecutionTime) + " seconds\n")

    fobj.close()

    # print("Execution Time : " + str(ExecutionTime) + " seconds")
    print(Border)
    print("--------------- Check Directory Log --------------")
    print("-------------------- Thank You -------------------")
    print(Border)

if __name__ == "__main__":
    main()