import os
import sys
import FileUtils

def main():
    Border = "-"*50
    print(Border)
    print("--------------- Directory Copy Log ---------------" )
    print(Border)

    if (len(sys.argv) != 4):
        print("Invalid number of arguments")
        return
    
    FirstDirectory = sys.argv[1]
    SecondDirectory = sys.argv[2]
    Extension = sys.argv[3]

    fobj = open("DirectoryLog3.log", "w")
    fobj.write(Border + "\n")
    fobj.write("This is a log file\n")
    fobj.write(Border + "\n")
    
    FileUtils.DirectoryCopySpecific(FirstDirectory, SecondDirectory, Extension, fobj)

    fobj.close()
    print(Border)
    print("--------------- Check Directory Log 3 ------------")
    print("-------------------- Thank You -------------------")
    print(Border)  

if __name__ == "__main__":
    main()

# python3 program31_4.py SourceFolder1 DestFolder2 doc - command