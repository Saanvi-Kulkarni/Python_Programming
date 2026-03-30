from functools import reduce

def ChkPrime(No):
    if No < 2:
        return False
    
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

Multiply = lambda No: No*2  

def Max(No1, No2):
    if(No1 > No2):
        return No1
    else:
        return No2

def main():
    Size = 0
    Value = 0

    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(ChkPrime, Data))
    print("List after filter : ", FData)

    MData = list(map(Multiply, FData))
    print("List after Map : ", MData)

    RData = reduce(Max, MData)
    print("List after reduce : ", RData)

if __name__ == "__main__":
    main()