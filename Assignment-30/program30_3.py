import os
import sys

def main():
    FileName = sys.argv[1]

    Ret = os.path.exists(FileName)

    if Ret == True:
        fobj = open(FileName,'r')
        Data = fobj.readlines()
        fobj.close()

        for i in range(len(Data)):
            print(Data[i], end = " ")
        print("")

    else:
        print("File not found")

if __name__ == "__main__":
    main()