def Addition(No1, No2):
    print("Addition is : ", No1+No2)

def Subtraction(No1, No2):
    print("Subtraction is : ", No1-No2)

def Multiplication(No1, No2):
    print("Multiplication is : ", No1*No2)

def Division(No1, No2):
    print("Division is : ", No1/No2)

def main():
    Value1 = 0
    Value2 = 0

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Addition(Value1,Value2)
    Subtraction(Value1,Value2)
    Multiplication(Value1,Value2)
    Division(Value1,Value2)

if __name__ == "__main__":
    main()