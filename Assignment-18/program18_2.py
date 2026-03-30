def Max(Arr):
    Max = Arr[0]

    for i in range(len(Arr)):
        if (Arr[i] > Max):
            Max = Arr[i]
    return Max

def main():
    Size = 0
    Value = 0

    print("Enter number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = Max(Data)
    print("Maximum is : ", Ret)

if __name__ == "__main__":
    main()