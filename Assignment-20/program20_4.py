import threading

def Small(Str):
    Count = 0
    for i in range(len(Str)):
        if(Str[i].islower()):
            Count = Count + 1

    t = threading.current_thread()
    print("Thread ID (capital): ", t.ident)
    print("Thread name : ", t.name)
    print("Count of small : ", Count)

def Capital(Str):
    Count = 0
    for i in range(len(Str)):
        if(Str[i].isupper()):
            Count = Count + 1
    
    t = threading.current_thread()
    print("Thread ID (capital): ", t.ident)
    print("Thread name : ", t.name)
    print("Count of capital : ", Count)

def Digits(Str):
    Count = 0
    for i in range(len(Str)):
        if(Str[i].isdigit()):
            Count = Count + 1

    t = threading.current_thread()
    print("Thread ID (capital): ", t.ident)
    print("Thread name : ", t.name)
    print("Count of digits : ", Count)

def main():
    Sentence = input("Enter string : ")

    t1 = threading.Thread(target = Small, args = (Sentence,))
    t2 = threading.Thread(target = Capital, args = (Sentence,))
    t3 = threading.Thread(target = Digits, args = (Sentence,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()