def Factorial(No):
    i = 0
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i
    return Fact

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = Factorial(Value)

    print("Factorial is : ", Ret)

if __name__ == "__main__":
    main()