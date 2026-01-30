def ReverseNo(No):
    Digit = 0
    ReverseNumber = 0

    while(No != 0):
        Digit = No % 10
        ReverseNumber = (ReverseNumber * 10) + Digit
        No = No // 10

    return ReverseNumber

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = ReverseNo(Value)

    print("Reverse Number is : ", Ret)

if __name__ == "__main__":
    main() 