def ChkFreq(Arr, No):
    Frequency = 0

    for i in range(len(Arr)):
        if (Arr[i] == No):
            Frequency = Frequency + 1
    return Frequency

def main():
    Size = 0
    Value = 0
    Number = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Enter a number to check frequency in list : ")
    Number = int(input())

    Ret = ChkFreq(Data, Number)
    print("Frequency of number is : ", Ret)

if __name__ == "__main__":
    main()