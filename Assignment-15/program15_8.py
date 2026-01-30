# def ChkDivisible(No):
#     return((No % 3 == 0) and (No % 5 == 0))

ChkDivisible = lambda No: ((No % 3 == 0) and (No % 5 == 0))

def main():
    Size = 0
    Value = 0

    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Original data is : ", Data)

    FData = list(filter(ChkDivisible, Data))

    print("Data after filter is : ", FData)

if __name__ == "__main__":
    main()