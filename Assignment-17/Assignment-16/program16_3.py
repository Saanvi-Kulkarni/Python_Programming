def ChkNum(No1, No2):
    return(No1 + No2)

def main():
    Value1 = 0
    Value2 = 0
    iRet = 0

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    iRet = ChkNum(Value1, Value2)

    print("Addition is : ", iRet)

if __name__ == "__main__":
    main()