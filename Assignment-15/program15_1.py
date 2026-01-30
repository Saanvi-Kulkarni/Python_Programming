# def DisplaySq(No):
#     return No**2

DisplaySq = lambda No: No**2

def main():
    Size = 0
    Value = 0

    Size = int(input("Enter number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Actual input is : ", Data)

    MData = list(map(DisplaySq, Data))

    print("Data after map is : ", MData)

if __name__ == "__main__":
    main()