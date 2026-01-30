def ChkPalindrom(No):
    Digit = 0
    OriginalNumber = No
    ReverseNumber = 0

    while(No != 0):
        Digit = No % 10
        ReverseNumber = (ReverseNumber * 10) + Digit
        No = No // 10

    print(ReverseNumber)

    if(OriginalNumber == ReverseNumber):
        return True
    else:
        return False

def main():
    Value = 0
    Ret = False

    Value = int(input("Enter number : "))

    Ret = ChkPalindrom(Value)

    if(Ret == True):
        print("Number is Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main() 