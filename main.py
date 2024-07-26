from bank import Bank

def main():
    bank = Bank()
    
    while True:
        print("\nWelcome to Agicious Bank PLC\n")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Exit")
        choice = input("Enter your preferred choice")
        
        if choice == "1":
            name = input("enter name: ")
            initial_deposit =  float(input("enter initial deposit amount"))
            bank.create_account(name, initial_deposit)
            
        elif choice == "2":
            name = input("Enter your name: ")
            amount = float(input("Enter Deposit amount: "))
            bank.deposit(name, amount)    
            
        elif choice == "3":
            name = input("enter your name: ")
            amount = float(input("enter your withdrawal amount: "))
            bank.withdraw (name, amount)
            
        elif choice == "4":
            name = input("enter your account name")
            bank.check_balance(name)       
            
        elif choice == "5":
            print("Thank you for banking with us!")
            break
            
        else:
            print("Invalid choice entered. please try again")   
      
if __name__ == main():
        main()                 
        