def Multiplication(No):
    i = 0
    Multiplication = 1

    for i in range(1,11):
        Multiplication = No * i
        print(Multiplication) 

def main():
    Value = 0

    Value = int(input("Enter number : "))

    Multiplication(Value)

if __name__ == "__main__":
    main()