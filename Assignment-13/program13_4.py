def ConvertBinary(No):
    Remainder = 0
    BinaryNumber = " "

    while(No > 0):
        Remainder = No % 2
        BinaryNumber = str(Remainder) + BinaryNumber
        No = No // 2

    return BinaryNumber
        
def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = ConvertBinary(Value)

    print("Binary number is : ", Ret)

if __name__ == "__main__":
    main()