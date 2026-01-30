def DisplayCube(No):
    Cube = 0

    Cube = No**3

    return Cube

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = DisplayCube(Value)
    print("Cube of number is : ", Ret)

if __name__ == "__main__":
    main()