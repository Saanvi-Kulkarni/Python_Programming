import os
import sys
import FileUtils

def main():
    Border = "-"*50
    print(Border)
    print("---------------- Directory Log 1 -----------------")

    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        return
    
    DirName = sys.argv[1]
    OldExtension = sys.argv[2]
    NewExtension = sys.argv[3]

    fobj = open("DirectoryLog1.log", "a")

    fobj.write(Border + "\n")
    fobj.write("This is a log file\n")
    fobj.write(Border + "\n")

    FileUtils.RenameFile(DirName, OldExtension, NewExtension, fobj)

    fobj.write(Border + "\n")
    print("-------------- Check Directory Log 1 -------------")
    fobj.write("-------------------- Thank You -------------------\n")
    fobj.write(Border + "\n")

    fobj.close()

if __name__ == "__main__":
    main()