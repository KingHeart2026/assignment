print( '''
        WELCOME TO KING HEART BANK
INSERT YOUR CARD
''')
balance = 560000000
print("1. Check balance")
print("2. Withdraw Money")
print("3. Deposit Money")

choice = int(input("choose an option:  "))

userpin = input("ENTER YOUR PIN: ")
if choice == 1:
        print ("it is:#",balance)
elif choice == 2:
        amount = float(input("Enter to withdraw:  "))

        if amount >0:
                if amount <= balance :
                        balance = balance - amount
                        print("Writhdrawal successful")
                        print ("Your new balance is #", balance)
                else: 
                        print("insufficient balance")
        else:
                print("amount must be greater than 0")

elif  choice == 3:
        amount = float(input("Enter the amount of deposit:  "))
        if amount >0:
                        balance = balance + amount
                        print("Deposit successful ")
                        print("Your new balance is #", balance)
        else:
                print("Amount must be greater than 0")

else:
     print("Invalid option")