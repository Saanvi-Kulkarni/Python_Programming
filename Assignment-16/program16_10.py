def DisplayLen(Name):
    Count= 0 

    for i in Name:
        # print(i)
        Count = Count + 1

    return Count

def main():
    Value =str(input("Enter name : "))

    iRet = DisplayLen(Value)

    print("Count is : ", iRet)

if __name__ == "__main__":
    main()