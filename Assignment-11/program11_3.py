def SumDigits(No):
    Sum = 0

    while(No != 0):
        Digit = No % 10
        
        No = No // 10

        Sum = Sum + Digit
        print(Sum)

    return Sum

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = SumDigits(Value)

    print("Sum of digits : ", Ret)

if __name__ == "__main__":
    main()