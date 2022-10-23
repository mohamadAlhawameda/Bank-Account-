balance = 500
def show_balance(balance):
        print(f"Your balance is {balance:0.2f}")
def can_withdraw( balance, value):
    if(balance < value):
        print(f"Not enought in the bank to withdraw {value}")
        return False
    return True

def withdraw(balance):
    choic = int(input("How much would you like to withdraw 1:20 2:40 3:60 4:80 5:100 6:Custom?: "))
    if(choic ==1):
        if can_withdraw(balance, 20):
            balance -= 20
            print(f"Balance deduced by 20, your new balance is {balance:0.2f}")
    elif (choic == 2):
        if can_withdraw(balance, 40):
            balance -= 40
            print(f"Balance deduced by 40, your new balance is {balance:0.2f}")
    elif(choic == 3):
        if can_withdraw(balance, 60):
            balance -=60
            print(f"Balance deduced by 40, your new balance is {balance:0.2f}")
    elif(choic == 4):
        if can_withdraw(balance, 80):
            balance -=80
            print(f"Balance deduced by 80, your new balance is {balance:0.2f}")
    elif(choic == 5):
        if can_withdraw(balance, 100):
            balance -=100
            print(f"Balance deduced by 100, your new balance is {balance:0.2f}")
    elif(choic == 6):
        try:
            custom = int(input("How much woudl you like to withdraw from your account: "))
            if can_withdraw(balance, custom):
                balance -=custom
                print(f"Balance deduced by {custom} your new balance is {balance:0.2f}")
        except ValueError:
            print("This is not int")
        return balance
def deposit(balance):
    try:
        newCh = int(input("How much would you like to add: "))
        balance = balance + newCh
        print(f"New balance is {balance:0.2f}")
        return balance
    except ValueError:
        print("Please enter an int")
for attemp in range(1, 4):
    try:
        pin = int(input("What is your pin? "))
        if(pin != 1234):
            if(attemp == 3):
                print("Pin invalide 3 times...")
                exit()
        else:
            break
    except ValueError:
        print("Please enter an int")
print("Your singed in")

while(True):
    print("This is main menu")
    print("1 to display the balance\n2 will allow making a withdrawal\n3 will allow making a deposit\n4 will exit the program")
    myinput=int(input("Please choose one of the folooiwing?: "))
    if(myinput == 1):
        balance = show_balance(balance)
    elif(myinput == 2):
        balance = withdraw(balance)
    elif(myinput == 3):
        balance = deposit(balance)
    elif(myinput == 4):
        print("Thank you for youe visit\nHave a great day!")
        exit()

    if(input("Would you like to exit(Y/N)? ").lower() == "Y"):
        exit()     


