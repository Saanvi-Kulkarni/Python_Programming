import Arithmatic

print("Inside program : ", __name__)

Value1 = int(input("Enter fisrt number : "))
Value2 = int(input("Enter second number : "))

Result = 0

Result = Arithmatic.Add(Value1, Value2)
print("Addition is : ", Result)

Result = Arithmatic.Sub(Value1, Value2)
print("Subtraction is : ", Result)

Result = Arithmatic.Mult(Value1, Value2)
print("Multiplication is : ", Result)

Result = Arithmatic.Div(Value1, Value2)
print("Division is : ", Result)