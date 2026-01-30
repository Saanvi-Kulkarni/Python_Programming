def AreaRect(l, b):
    Area = 0

    Area = l * b

    return Area

def main():
    length = 0
    width = 0
    Ret = 0

    length = int(input("Enter length of rectangle : "))
    width = int(input("Enter width of rectangle : "))

    Ret = AreaRect(length, width)

    print("Area of rectangle is : ", Ret)

if __name__ == "__main__":
    main()