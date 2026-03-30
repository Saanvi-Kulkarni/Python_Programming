import threading

Counter = 0
Lock = threading.Lock()

def IncrementCounter(No):
    global Counter

    for i in range(No):
        Lock.acquire()
        Counter = Counter + 1
        Lock.release()

def main():
    t1 = threading.Thread(target = IncrementCounter, args = (5,),)
    t2 = threading.Thread(target = IncrementCounter, args = (5,),)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final value of counter is : ", Counter)

if __name__ == "__main__":
    main()