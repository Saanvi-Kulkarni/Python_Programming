# def ChkEven(No):
#     return (No % 2 == 0)

ChkEven = lambda No: (No % 2 == 0)

def main():
    Size = 0
    Value = 0

    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Actual data is : ", Data)

    FData = list(filter(ChkEven, Data))

    print("Data after filter is : ", FData)

if __name__ == "__main__":
    main()