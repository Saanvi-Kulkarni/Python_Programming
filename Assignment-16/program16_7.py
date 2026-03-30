def ChkDivisible(No):
    if(No % 5 == 0):
        return True
    else:
        return False

def main():
    Value = 0
    bRet = False

    Value = int(input("Enter number : "))

    bRet = ChkDivisible(Value)

    print(bRet)

if __name__ == "__main__":
    main()