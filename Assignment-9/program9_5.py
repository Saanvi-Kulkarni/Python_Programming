def ChkDivisible(Value):
    if((Value % 3 == 0) and (Value % 5 == 0)):
        return True
    else:
        return False

def main():
    No = 0
    Ret = False

    No = int(input("Enter number : "))

    Ret = ChkDivisible(No)

    # print(Ret)

    if(Ret == True):
        print("Divisible by 3 & 5")
    else:
        print("Not Divisible by 3 & 5")

if __name__ == "__main__":
    main()