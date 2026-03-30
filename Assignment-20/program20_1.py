import threading
import time

def ChkEven(No):
    print("Even numbers are : ")
    for i in range(2,No+1,2):
        print(i)
    

def ChkOdd(No):
    print("Odd numbers are : ")
    for i in range(1,No+1,2):
        print(i)

def main():
    start_time = time.time()

    t1 = threading.Thread(target = ChkEven, args = (20,))
    t2 = threading.Thread(target = ChkOdd, args = (20,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()

if __name__ == "__main__":
    main()