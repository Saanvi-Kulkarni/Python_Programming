import threading

def Maximum(Arr):
    Max = 0
    Max = Arr[0]

    for i in range(len(Arr)):
        if(Arr[i] > Max):
            Max = Arr[i]
    print("Maximum element is : ", Max)

def Minimum(Arr):
    Min = 0
    Min = Arr[0]

    for i in range(len(Arr)):
        if(Arr[i] < Min):
            Min = Arr[i]
    print("Minimum element is : ", Min)

def main():
    Size = 0
    Value = 0

    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target = Maximum, args = (Data,),)
    t2 = threading.Thread(target = Minimum, args = (Data,),)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()