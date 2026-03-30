import MarvellousNum

def ListPrime(Arr):
    Sum = 0

    for i in range(len(Arr)):
        if MarvellousNum.ChkPrime(Arr[i]):
            Sum = Sum + Arr[i]

    return Sum

def main():
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = ListPrime(Data)
    print("Addition of all prime numbers : ", Ret)

if __name__ == "__main__":
    main()