def DisplaySquare(No):
    Square = 0
    
    Square = No**2
    
    return Square

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = DisplaySquare(Value)
    print("The square of number is : ", Ret)

if __name__ == "__main__":
    main()