ChkOdd = lambda No: (No % 2 != 0)

def main():
    Value = int(input("Enter number : "))

    Ret = ChkOdd(Value)

    if (Ret == True):
        # print("It is Even")
        print(Ret)
    else:
        # print("It is Odd")
        print(Ret)

if __name__ == "__main__":
    main()
