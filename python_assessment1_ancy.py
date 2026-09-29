class bank_details:
  

    def __init__(self,number,name,pin,password):
        self.account_number=number
        self.user_name=name
        self.bank_pin=pin
        self.bank_password=password
        self.balance=0

    def account_login(self,user_input,pin_input):
        if (user_input==self.account_number or
                user_input==self.user_name)and pin_input==self.bank_pin:
            print("Yes, Correct username/account number and PIN")
            return True
        else:
            print("Invalid details......!")
            return False

    def deposit(self,amount):
        if amount>0:
            self.balance =self.balance+amount
            print("Deposit Successful.........!")
            print("Current Balance....:",self.balance)
        else:
            print("Deposit amount should greter than 0...!!")

    def withdrawal(self,amount):
        if amount<= 0:
            print("Withdrawal amount should greater than 0...!!")
        elif amount>self.balance:
            print("Insufficient balance.........!")
        else:
            self.balance =self.balance-amount
            print("Withdrawal Successful.......!")
            print("Remaining Balance is ..:",self.balance)

account1=bank_details("11","ancy","763","rain123")
account2=bank_details("12","rani","888","vest123")
accounts=[account1,account2]
user_input=input("Enter AccountNumber or Username...: ")
pin_input=input("Enter PIN:")

for account in accounts:
    if account1.account_login(user_input,pin_input):
        amount = float(input("Enter deposit amount..:"))
        account1.deposit(amount)
        withdrawal_amount = float(input("Enter withdrawal amount...:"))
        account1.withdrawal(withdrawal_amount)
