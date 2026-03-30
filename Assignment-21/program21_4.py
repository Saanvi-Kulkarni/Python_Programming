import threading

def Summation(Arr):
    Sum = 0

    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
    print("Sum is : ", Sum)

def Multiplication(Arr):
    Product = 1

    for i in range(len(Arr)):
        Product = Product * Arr[i]
    print("Product is : ", Product)

def main():
    Size = 0
    Value = 0

    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target = Summation, args = (Data,),)
    t2 = threading.Thread(target = Multiplication, args = (Data,),)

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()