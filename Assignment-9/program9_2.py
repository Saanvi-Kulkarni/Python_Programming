def ChkGreater(No1, No2):
    if(No1 > No2):
        print("Greater number is : ", No1)
    else:
        print("Greater number is : ", No2)


def main():
    Value1 = 0
    Value2 = 0

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    ChkGreater(Value1, Value2)

if __name__ == "__main__":
    main()