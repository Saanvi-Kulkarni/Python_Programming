def ChkNum(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    Value = 0
    bRet = False
    Value = int(input("Enter number : "))

    bRet = ChkNum(Value)

    if(bRet == True):
        print("Even Number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()