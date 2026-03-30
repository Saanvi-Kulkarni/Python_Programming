import os

def main():
    FileName = input("Enter file name : ")
    
    Ret = os.path.exists(FileName)

    if(Ret == True):
        fobj = open(FileName, 'r')
        print("File gets successfully opened")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()