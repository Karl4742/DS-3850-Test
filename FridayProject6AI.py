class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} has been deposited.")
        else:
            print("Please enter a positive amount to deposit.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} has been withdrawn.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Please enter a positive amount to withdraw.")

    # Method to check balance
    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

# Create one account instance
account = BankAccount(account_number="123456")

# Main program loop
while True:
    print("\nWelcome to the Bank Account Program")
    entered_account_number = input("Please enter your account number: ").strip()

    # Check if the entered account number matches
    if entered_account_number == account.account_number:
        print("\nOptions:")
        print("a) Deposit money")
        print("b) Withdraw money")
        print("c) Check balance")
        print("q) Quit")

        choice = input("Choose an option (a/b/c/q): ").strip().lower()

        if choice == "a":
            try:
                deposit_amount = float(input("Enter amount to deposit: "))
                account.deposit(deposit_amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "b":
            try:
                withdraw_amount = float(input("Enter amount to withdraw: "))
                account.withdraw(withdraw_amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "c":
            account.check_balance()

        elif choice == "q":
            print("Thank you for using the Bank Account Program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a, b, c, or q.")
    else:
        print("Account number not recognized. Please try again.")
