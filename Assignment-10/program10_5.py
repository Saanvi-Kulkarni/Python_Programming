def DisplayOdd(No):
    i = 0

    for i in range(1,No+1):
        if(i % 2 != 0):
            print(i)

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    DisplayOdd(Value)

if __name__ == "__main__":
    main()