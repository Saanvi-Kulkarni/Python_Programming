def Count(No):
    Cnt = 0

    while(No != 0):
        Digit = No % 10
        Cnt = Cnt + 1
        No = No // 10

    return Cnt

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = Count(Value)
    print("Number of digits are : ", Ret)

if __name__ == "__main__":
    main()