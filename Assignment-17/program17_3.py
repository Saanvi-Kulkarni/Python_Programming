
def DisplayFact(No):
    Factorial = 1

    for i in range(No, 0, -1):
        Factorial = Factorial * i
        # print(Factorial)

    return Factorial

def main():
    Value = int(input("Enter number : "))

    iRet = DisplayFact(Value)

    print("Factorial is : ", iRet)

if __name__ == "__main__":
    main()