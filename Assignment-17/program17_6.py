def Display(No):

    for i in range(No, 0, -1):
        for j in range(1, i+1):
            print("*    ", end = " ")
            
        print(" ")

def main():
    Value = int(input("Enter number : "))

    Display(Value)

if __name__ == "__main__":
    main()

# 1,1     1,2     1,3     1,4
# 2,1     2,2     2,3     
# 3,1     3,2         
# 4,1          