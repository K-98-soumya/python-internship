class SBI:
    branch_code = 7056
    maintainance_amt = 100
    def __init__(self, name, mob_no,age):
        self.Acc_holder_name = name 
        self.Mob_no = mob_no
        self.age = age
        self.balance = 0
        
    def deposoite(self, amt):
        self.balance = self.balance + amt
        
    def withdraw(self,amt):
        if(self.balance>= amt):
            self.balance = self.balance - amt
            return"sufficient balance"
        else:
            print("Insufficient balance")
        
    def transfer(self,sender_acc, amt):
        transfer_condtion = sender_acc.withdraw( amt )
        if(transfer_condtion == "sufficient balance"):
            self.deposoite(amt)
            
    def print_balance(self):
        print(self.balance)
        
soumya_acc = SBI("soumya","8121235455","27")
tejas_acc = SBI("tejas","129884578","12")
soumya_acc.deposoite(34000)
tejas_acc.deposoite(1000000)
soumya_acc.withdraw(10000)
print(soumya_acc.balance)
soumya_acc.transfer(tejas_acc,34000)
print(soumya_acc.balance)
print(tejas_acc.balance)

            
        
