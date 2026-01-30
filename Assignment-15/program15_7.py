# def ChkGreater(No):
#     return len(No) > 5

ChkGreater = lambda No: len(No) > 5

def main():
    Size = 0
    Value = 0

    Size = int(input("Enter number of elements : "))

    Data = list()
    
    print("Enter the elements : ")

    for i in range(Size):
        Value = str(input())
        Data.append(Value)

    print("Actual data is : ", Data)

    FData = list(filter(ChkGreater, Data))

    print("Data after filter is : ", FData)

if __name__ == "__main__":
    main()