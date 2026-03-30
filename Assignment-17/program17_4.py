def SumFactor(No):
    Sum = 0

    for i in range(1, No):
        if(No % i == 0):
            Sum = Sum + i
            print(i)
    return Sum

def main():
    Value = int(input("Enter number : "))

    iRet = SumFactor(Value)

    print("Sum of Factors is : ", iRet)

if __name__ == "__main__":
    main()