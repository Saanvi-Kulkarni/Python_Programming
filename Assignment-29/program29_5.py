import os
import sys

def main():
    FileName = sys.argv[1]
    str = sys.argv[2]
    
    Ret = os.path.exists(FileName)

    if(Ret == True):
        fobj = open(FileName, 'r')
        Data = fobj.read()
        fobj.close()

        Count = Data.count(str)

        print("Frequency is : ", Count)

    else:
        print("There is no such file")

if __name__ == "__main__":
    main()