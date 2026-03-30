def Display(No):

    for i in range(1, No+1):
        for j in range(i):
            print(j+1 , end = " ")
            
        print(" ")

def main():
    Value = int(input("Enter number : "))

    Display(Value)

if __name__ == "__main__":
    main()        

# 1,1     
# 2,1     2,2     
# 3,1     3,2     3,3     
# 4,1     4,2     4,3     4,4