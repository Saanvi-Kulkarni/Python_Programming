def IsPrime(No):
    if(No < 1):
        return False

    for i in range(2, No):
        if(No % i == 0):
            return False
    return True

def main():
    bRet = False

    Value = int(input("Enter number : "))

    bRet = IsPrime(Value)

    if(bRet == True):
        print("It is a prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()