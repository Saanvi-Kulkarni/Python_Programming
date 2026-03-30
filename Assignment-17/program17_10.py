def SumDigits(No):
    Summation = 0

    while(No != 0):
        Digit = No % 10
        Summation = Summation + Digit
        No = No // 10
    
    return Summation

def main():
    Value = int(input("Enter number : "))

    Ret = SumDigits(Value)
    print("Sum of digits is : ", Ret)

if __name__ == "__main__":
    main()