class Numbers:
    
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if (self.Value < 2):
            return False
        for i in range(2,self.Value+1):
            if(self.Value % i == 0):
                return False
        return True
    
    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value+1):
            if(self.Value % i == 0):
                Sum = Sum + i

        return Sum
    
    def ChkPerfect(self):
        Sum = self.SumFactors()
        if Sum - self.Value == self.Value:
            return True
        else:
            return False
        
    def Factors(self):
        print("Factors are : ")
        for i in range(1, self.Value+1):
            if(self.Value % i == 0):
                print(i)

def main():
    obj1 = Numbers(10)
    print("Number : ", obj1.Value)
    print("Prime   : ", obj1.ChkPrime())
    print("Perfect : ", obj1.ChkPerfect())
    obj1.Factors()
    print("Sum of Factors : ", obj1.SumFactors())

if __name__ == "__main__":
    main()