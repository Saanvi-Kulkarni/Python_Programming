from functools import reduce

# def DisplayProduct(A, B):
#     return(A * B)

DisplayProduct = lambda A, B: (A * B)

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

    RData = reduce(DisplayProduct, Data)

    print("Data after reduce is : ", RData)

if __name__ == "__main__":
    main()