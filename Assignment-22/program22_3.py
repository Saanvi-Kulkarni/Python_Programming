class Arithmatic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter first number : "))
        self.value2 = int(input("Enter second number : "))

    def Addition(self):
        Ans = 0
        Ans = self.value1 + self.value2
        print("Addition is : ", Ans)
    
    def Subtraction(self):
        Ans = 0
        Ans = self.value1 - self.value2
        print("Subtraction is : ", Ans)
    
    def Multiplication(self):
        Ans = 0
        Ans = self.value1 * self.value2
        print("Multiplication is : ", Ans)
    
    def Division(self):
        Ans = 0
        try:
            Ans = self.value1 // self.value2
            print("Division is : ", Ans)
        except ZeroDivisionError:
            print("Cannot divide by zero")
        finally:
            print(" ")
    
def main():
    obj1 = Arithmatic()
    obj1.Accept()
    obj1.Addition()
    obj1.Subtraction()
    obj1.Multiplication()
    obj1.Division()

    print("-"*20)

    obj2 = Arithmatic()
    obj2.Accept()
    obj2.Addition()
    obj2.Subtraction()
    obj2.Multiplication()
    obj2.Division()

if __name__ == "__main__":
    main()