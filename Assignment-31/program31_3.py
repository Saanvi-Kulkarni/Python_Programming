import sys
import os
import FileUtils

def main():
    Border = "-"*50
    print(Border)
    print("--------------- Directory Copy Log ---------------")
    print(Border)

    if (len(sys.argv) != 3):
        print("Invalid number of arguments")
        return
    
    FirstDirectory = sys.argv[1]
    SecondDirectory = sys.argv[2]

    fobj = open("DirectoryLog2.log", "w")
    fobj.write(Border + "\n")
    fobj.write("This is a log file\n")
    fobj.write(Border + "\n")

    FileUtils.DirectoryCopy(FirstDirectory, SecondDirectory, fobj)

    fobj.close()
    print(Border)
    print("--------------- Check Directory Log 2 ------------")
    print("-------------------- Thank You -------------------")
    print(Border)    

if __name__ == "__main__":
    main()

# python3 program31_3.py SourceFolder1 DestFolder2 - command