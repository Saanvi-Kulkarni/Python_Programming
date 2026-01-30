import math

def AreaCircle(r):
    Area = 0

    Area = 3.14*r*r

    return Area

def main():
    radius = 0
    Ret = 0

    radius = int(input("Enter radius of circle : "))

    Ret = AreaCircle(radius)

    print("Area of circle is : ", Ret)

if __name__ == "__main__":
    main()