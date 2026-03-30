from functools import reduce

Product = lambda No1, No2: (No1 * No2)

IncreaseNo = lambda No: (No + 10)

ChkGreater = lambda No: No >= 70 and No <= 90

def main():
    Size = 0
    Value = 0

    print("Enter the size of list : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(ChkGreater,Data))
    print("List after Filter : ", FData)

    MData = list(map(IncreaseNo, FData))
    print("List after Map : ", MData)

    RData = reduce(Product, MData)
    print("List after Reduce : ", RData)

if __name__ == "__main__":
    main()