import os
import sys

def main():
    FileName = sys.argv[1]

    Ret = os.path.exists(FileName)

    if(Ret == True):
        fobj = open(FileName, 'r')
        Data = fobj.read()
        fobj.close()

        Words = Data.split()
        Count = len(Words)
        print("Total number of words : ", Count)

    else:
        print("File does not exist")

if __name__ == "__main__":
    main()