import sys
import os

def main():
    FileName = sys.argv[1]
    Ret = os.path.exists(FileName)

    if Ret == True:
        fobj = open(FileName,'r')
        Data = fobj.readlines()
        fobj.close()

        Count = len(Data)

        print("Total number of lines : ", Count)
    else:
        print("File does not exist")

if __name__ =="__main__":
    main()