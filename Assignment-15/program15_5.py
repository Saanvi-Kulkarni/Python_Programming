from functools import reduce

def Maximum(No1, No2):
    return max(No1, No2)

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

    RData = reduce(Maximum, Data)

    print("Data after reduce is : ", RData)

if __name__ == "__main__":
    main()
