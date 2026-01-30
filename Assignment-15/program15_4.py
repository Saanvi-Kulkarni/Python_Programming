from functools import reduce

# def Add(A, B):
#     return (A + B)

Add = lambda A, B: (A + B)

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

    RData = reduce(Add, Data)

    print("Data after reduce is : ", RData)

if __name__ == "__main__":
    main()