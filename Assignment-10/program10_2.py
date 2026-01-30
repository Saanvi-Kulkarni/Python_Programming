def SummationN(No):
    i = 0
    Sum = 0

    Sum = No * (No + 1) // 2

    return Sum 

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = SummationN(Value)

    print("Summation is : ", Ret)

if __name__ == "__main__":
    main()