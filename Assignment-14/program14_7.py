Divisible = lambda No: (No % 5 == 0)

def main():
    Value = int(input("Enter number : "))

    Ret = Divisible(Value)

    if (Ret == True):
        print(Ret)
    else:
        print(Ret)

if __name__ == "__main__":
    main()
