import os
import sys

def main():
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    Ret = os.path.exists(FileName1)

    if Ret == True:
        fobj1 = open(FileName1, 'r')
        Data = fobj1.read()

        fobj2 = open(FileName2, 'w')
        fobj2.write(Data)

    else:
        print("File does not exist")

if __name__ == "__main__":
    main()