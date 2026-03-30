import threading

def EvenFactor(No):
    sum = 0
    EvenList = []
    
    for i in range(1, No+1):
        if((No % i) == 0):
            if(i % 2 == 0):
                sum = sum + i
    print("Sum of even factors : ", sum) 

def OddFactor(No):
    sum = 0
    
    for i in range(1, No + 1):
        if((No % i) == 0):
            if(i % 2 != 0):
                sum = sum + i
    print("Sum of odd factors : ", sum) 

def main():
    Value = int(input("Enter number : "))

    t1 = threading.Thread(target = EvenFactor, args = (Value,))
    t2 = threading.Thread(target = OddFactor, args = (Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()