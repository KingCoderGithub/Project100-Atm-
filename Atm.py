class Atm (object) :
    
    def __init__(self, cardNumber, pinNumber) :
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    
    def checkBalalnce(self) :
        print ("Your Balance : 50,000")

        
    def widthdrawal(self, amount) :
         
        newAmpount = 50000 - amount
        
        print("You have withdrawn amount :" + str(amount) + "Your remaining balance is :" + str(newAmpount) )
        
def main() :
    card_number = input("Enter your card number:")
    pin_number = input("Enter your pin number:")
    newUser = Atm(card_number, pin_number)
    print("Choose your activity:")
    print("1 = Balance Enquiry   2 = Withdrawal")
    activity = int(input("Enter activity number:"))
    
    if(activity == 1):
        newUser.checkBalalnce()
    elif(activity == 2):
        amount = int(input("Enter the withdrawal Amount:"))
        newUser.widthdrawal(amount)
    else :
        print("Enter a valid number")
        
main()