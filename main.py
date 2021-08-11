import random
number = input("Enter your card number. =>")
pinno =  input("Enter your card pin =>")
balance = random.randint(200,500)
class atm(object):
    def __init__(self,cardno,pin):
        self.cardno = number
        self.pin = pinno
    def cashwithdrawal(self):
        print("Withdrawal Processing ! Thank you for chosing us.")
    def balanceenquiry(self):
        print("Your current balance is : " + str(balance))
atm1 = atm(number,pinno)    
useraction = input("Please enter the action to perform (just enter the number): \n1) Withdraw your cash \n2) Balance Enquiry")
if(int(useraction) == 1 ):
    atm1.cashwithdrawal()
elif(int(useraction) == 2):
    atm1.balanceenquiry()
