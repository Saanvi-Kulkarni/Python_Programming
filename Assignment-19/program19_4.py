from functools import reduce

Add = lambda No1, No2: No1 + No2

Square = lambda No: No**2   

ChkEven = lambda No: No % 2 == 0

def main():
    Size = 0
    Value = 0

    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(ChkEven, Data))
    print("List after filter : ", FData)

    MData = list(map(Square, FData))
    print("List after Map : ", MData)

    RData = reduce(Add, MData)
    print("List after reduce : ", RData)

if __name__ == "__main__":
    main()