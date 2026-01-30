def IsPrime(Value):
    if Value <= 1:
        return False

    for i in range (2,Value):
        if(Value % i == 0):
            return False
    return True    

def main():
    No = 0
    Ret = False

    No = int(input("Enter number : "))

    Ret = IsPrime(No)

    if(Ret == True):
        print("Prime Number")
    else:
        print("Not prime")

if __name__ == "__main__":
    main()