def ChkFactors(No):
    Factor = 0

    for i in range(No,0,-1):
        print(i)

def main():
    Value = 0
    Ret = False

    Value = int(input("Enter number : "))

    Ret = ChkFactors(Value)

if __name__ == "__main__":
    main()