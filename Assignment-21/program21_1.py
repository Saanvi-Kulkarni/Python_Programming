import threading

def ChkPrime(No):
    if(No < 2):
        return False
    
    for i in range(2, No):
        if(No % i == 0):
            return False
    return True

def Prime(Arr):
    print("Prime numbers : ")
    for i in range(len(Arr)):
        if ChkPrime(Arr[i]):
            print(Arr[i])

def NonPrime(Arr):
    print("NonPrime numbers : ")
    for i in range(len(Arr)):
        if not ChkPrime(Arr[i]):
            print(Arr[i])

def main():
    Size = 0
    Value = 0

    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target = Prime, args = (Data,),)
    t2 = threading.Thread(target = NonPrime, args = (Data,),)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()