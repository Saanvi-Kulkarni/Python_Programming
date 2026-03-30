import os

def main():
    FileName = input("Enter name of file : ")

    Ret = os.path.exists(FileName)

    try:
        if(Ret == True):
            # fobj = open(FileName,'w')
            # print("File gets opened and content is written in the file")

            # fobj.write("Jay Ganesh ...")

            fobj = open(FileName,'r')

            Data = fobj.read()
            print("Data of file is : ", Data)

            fobj.close()

    except FileNotFoundError:
        print("There is no such file")

if __name__ == "__main__":
    main()