import threading

def EvenList(Arr):
    print("List of even numbers : ")
    for i in range(len(Arr)):
        if (Arr[i] % 2 == 0):
            print(Arr[i])

def OddList(Arr):
    print("List of odd numbers : ")
    for i in range(len(Arr)):
        if (Arr[i] % 2 != 0):
            print(Arr[i])

def main():
    Size = 0
    Value = 0

    Size = int(input("Enter number of elements : "))

    Data = list()

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target = EvenList, args = (Data,))
    t2 = threading.Thread(target = OddList, args = (Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()