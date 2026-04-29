import sys
import os
import FileUtils

def main():
    Border = "-"*50
    print(Border)
    print("----------------- Directory Log ------------------")
    print(Border)

    if (len(sys.argv) != 3):
        print("Invalid number of arguments")
        return

    DirName = sys.argv[1]
    Extension = sys.argv[2]

    fobj = open("DirectoryLog.log", "w")

    fobj.write(Border + "\n")
    fobj.write("This is a log file\n")
    fobj.write(Border + "\n")

    FileUtils.DirectoryScan(DirName, Extension, fobj)

    fobj.close()

    print(Border)
    print("--------------- Check Directory Log --------------")
    print("-------------------- Thank You -------------------")
    print(Border)

if __name__ == "__main__":
    main()