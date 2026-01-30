# def Max(No1, No2):
#     return Max(No1, No2)

Maximum = lambda No1, No2: max(No1, No2)

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Maximum(Value1, Value2)

    print("Maximum is : ", Ret)

if __name__ == "__main__":
    main()
