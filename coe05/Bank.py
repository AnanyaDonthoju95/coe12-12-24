class Bank:
    def viewOptions(self):
        print("1. Deposit\n2. Withdraw\n3. Balance Enquiry\n4. Exit")
    def Deposit(self):
        amount=int(input("Enter to amount to deposit"))
        if 100<amount<50000 and amount%100==0:
            print("amount deposited successfully")
        else:
            print("Unable to deposit")

    def withdraw(self):
        accbal=10000
        for attempts in range(3):
            amount=int(input("Enter amount to withdraw"))
            if amount%100==0 and 100<amount<20000 and amount<accbal and accbal-amount>500:
                print("Withdrawal successfull")
            else:
                print("unable to complete withdrawal")
                attempts+=1
        if attempts==3:
            print("Exceeded withdrawal limit")
    def validation(self):
        for attempts in range(3):
            pin = int(input("Enter PIN: "))
            if pin == 1234:
                self.viewOptions()
                break
            else:
                print("Invalid PIN")
                attempts += 1

        if attempts == 3:
            print("Too many incorrect attempts.")
obj = Bank()
obj.validation()
obj.Deposit()
obj.withdraw()