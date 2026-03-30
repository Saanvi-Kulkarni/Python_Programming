import sys
import os

def main():
    FileName = sys.argv[1]

    Ret = os.path.exists(FileName)

    if(Ret == True):
        fobj1 = open(FileName,'r')
        Data = fobj1.read()
        fobj1.close()

        fobj2 = open('Demo.txt','w')
        fobj2.write(Data)
        fobj2.close()

    print("Contents copied successfully")

if __name__ == "__main__":
    main()