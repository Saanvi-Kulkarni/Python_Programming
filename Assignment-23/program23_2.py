class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount
    
    def Display(self):
        print("Account holder : ", self.Name)
        print("Current Balance : ", self.Amount)

    def Deposit(self):
        deposit_amt = int(input("Enter deposit amount : "))
        self.Amount = self.Amount + deposit_amt

    def Withdraw(self):
        withdraw_amt = int(input("Enter withdraw amount : "))
        if(self.Amount > withdraw_amt):
            self.Amount = self.Amount - withdraw_amt
        else:
            print("Not enough balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest is : ", Interest)

def main():
    obj1 = BankAccount("Rohan Kolhatar", 80000)
    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInterest()
    obj1.Display()

    print("-"*20)

    obj2 = BankAccount("Aditi Kolhatkar", 90000)
    obj2.Display()
    obj2.Deposit()
    obj2.Withdraw()
    obj2.CalculateInterest()
    obj2.Display()

if __name__ == "__main__":
    main()
