def Display(No):
    for i in range(No):
        print("*    ", end="")

def main():
    Value = 0

    Value = int(input("Enter first number : "))

    Display(Value)

if __name__ == "__main__":
    main()