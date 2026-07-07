Simple ATM Simulator
#	Input: User PIN and transaction choice.
#	Process: Check balance, withdraw, deposit.
#	Output: Updated balance.

class BankAccount:
    def __init__(self,pin):
        self.min_balance=1000
        self.balance=self.min_balance
        self.upin=1234
        self.upin=pin
        
        if self.upin==pin:
            print("Pin Matched!")
        else:
            print("Enter Correct pin:")
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print("Deposited amount:", amount)
            print("Available Balance:",self.balance)    
        else:
            print("Deposit amount should be more than 0:")
    def withdraw(self,w_amount):
        if w_amount>0 and self.balance>=w_amount:
            self.balance=self.balance-w_amount 
            print("Withdrawn Amount is:",w_amount)
            print("Available Balance:",self.balance)
        else:
            print("Insufficient Balance or amount must be more than 0:")          
      
    def check_balance(self):
        print("Available Balance:",self.balance)
       
        

def main():
    
        pin=int(input("Enter your four digit pin:"))
        user=BankAccount(pin)
        while True:
            print("1: Deposit:")
            print("2: Withdraw amount:")
            print("3: Ckeck Balance:")
            choice=int(input("Enter your choice:"))
            if (choice==1):
                amount=int(input("enter the amount you want to deposit:"))
                user.deposit(amount)
            elif(choice==2):
                w_amount=int(input("enter the amount you want to withdraw:"))
                user.withdraw(w_amount)
            elif(choice==3):    
                user.check_balance()
                break
            else:
                print("Please Enter a correct choice:")
                main()    

main()            
