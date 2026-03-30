def DigitCount(No):
    Count = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        No = No // 10
        
        Count = Count + 1

    return Count

def main():
    Value = int(input("Enter number : "))
    
    Ret = DigitCount(Value)
    print("Number of digits are : ", Ret)

if __name__ == "__main__":
    main()