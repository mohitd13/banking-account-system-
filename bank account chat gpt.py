class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} into account {self.account_number}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account {self.account_number}: Balance = ${self.balance:.2f}"

def main():
    accounts = {}
    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                print("Account already exists.")
            else:
                accounts[account_number] = BankAccount(account_number)
                print(f"Account {account_number} created successfully.")

        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            if account_number in accounts:
                accounts[account_number].deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            if account_number in accounts:
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                balance = accounts[account_number].get_balance()
                print(f"Account {account_number} balance: ${balance:.2f}")
            else:
                print("Account not found.")

        elif choice == '5':
            print("Exiting the Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
