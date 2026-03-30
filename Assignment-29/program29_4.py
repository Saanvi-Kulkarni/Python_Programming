import sys

def main():
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    fobj1 = open(FileName1, 'r')
    Data1 = fobj1.read()

    fobj2 = open(FileName2, 'r')
    Data2 = fobj2.read()

    if(Data1 == Data2):
        print("Success")
    else:
        print("Failure")       

if __name__ == "__main__":
    main()