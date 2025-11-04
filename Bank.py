class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        #deposit positive ammounts into the account, do not allow invalid inputs
        #provide outputs to the user to tell them the outcome of the action
        pass


    def withdraw(self, amount):
        #reduce the balance in the account
        #do not let the balance fall below 0
        #provide confirmation of a successful withdrawl and the new balance
        pass


class SavingsAccount(BankAccount):
    #write the constructor for the savings account which inherits from the bank account.
    #the additional attributes of interest rate and minimum balance should be added
    pass

    def withdraw(self, amount):
        #withdraw from the savings account can not fall below the minium balance.
        #everytime a withdrawl is made successfully, the apply_interest method is run
        #after a successful withdrawl, a conformation is displayed and the new balance is shown
        pass

    def apply_interest(self):
        #calculate how much interest is to be added to the account and output a confirmation of the ammount
        pass

def main():
    print("Welcome to the Bank Account and Savings Account System")
    print("Creating a new Savings Account:")
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))
    interest_rate = float(input("Enter interest rate (in percentage): "))
    minimum_balance = float(input("Enter minimum balance: "))

    savings_account = SavingsAccount(account_number, account_holder, initial_balance, interest_rate, minimum_balance)

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Account Info")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            savings_account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            savings_account.withdraw(amount)
        elif choice == "3":
            #create get methods to then show the details of the account to the user
            pass
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
