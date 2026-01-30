def IsPerfect(No):
    Sum = 0

    for i in range(1, No):
        if(No % i == 0):
            print(i)
            Sum = Sum + i

    if(Sum == No):
        return True
    else:
        return False 


def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = IsPerfect(Value)

    if(Ret==True):
        print("It is a perfect number")
    else:
        print("It is not a perfect number")

if __name__ == "__main__":
    main()