import os
import sys

def main():
    FileName = sys.argv[1]
    Word = sys.argv[2]

    Ret = os.path.exists(FileName)

    if Ret == True:
        fobj = open(FileName, 'r')

        Data = fobj.read()

        fobj.close()

        if Word in Data:
            print(Word, " is present in file ", FileName)
        else:
            print(Word, " is not present in file ", FileName)
    else:
        print("File does not exist")

if __name__ == "__main__":
    main()