class Card:
    def __init__(self, pin):
        self.pin = pin
        self.inserted = False

    def insert(self):
        if self.inserted:
            return "Already, Card is inserted."
        self.inserted = True
        return "Card inserted accomplishly."

    def eject(self):
        if not self.inserted:
            return "There is no card to eject."
        self.inserted = False
        return "Card ejected. We wish you a good day, InfoSuper Bank."


class Account:
    def __init__(self, initial_balance=0): 
        self.balance = initial_balance

    def check_balance(self):
        return f"Your balance is: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount <= 0:
            return "Please enter a valid amount."
        self.balance += amount
        return f"${amount:.2f} deposited accomplishly! New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Please enter a valid amount."
        if amount > self.balance:
            return "Not enough money!"
        self.balance -= amount
        return f"${amount:.2f} withdrawn accomplishly! New balance: ${self.balance:.2f}"


class Transaction:

    transaction_type = "generic transaction"  

    @staticmethod
    def process_pin(card, entered_pin):
        if not card.inserted:
            return "Insert your card first."
        if card.pin == entered_pin:
            return "Welcome, PIN is correct."
        return "Incorrect PIN. Please try again."

    @staticmethod
    def receipt(action, amount, balance):
        return (
            f"--- RECEIPT ---DETAILED----\n"
            f"Action: {action}\n"
            f"Amount: ${amount:.2f}\n"
            f"New Balance: ${balance:.2f}\n"
        )


class ATM:
    def __init__(self):
        self.card = Card(pin="3534")
        self.account = Account()  
        self.pin_verified = False

    def start(self):
        while True:
            print("\n--- InfoSuper Bank ATM ---")
            if not self.card.inserted:
               
                print("1. Insert Card")
                print("2. Exit")
                choice = input("Choose an option: ")
                if choice == "1":
                    print(self.card.insert())
                elif choice == "2":
                    print("Thanks! InfoSuper Bank wishes you a good day!")
                    break
                else:
                    print("Invalid option. Try again.")
            elif not self.pin_verified:
              
                print("1. Enter Password")
                print("2. Cancel")
                choice = input("Choose an option: ")
                if choice == "1":
                    print("Hint: The default PIN is 3534")
                    entered_pin = input("Enter your four digit PIN: ")
                    pin_result = Transaction.process_pin(self.card, entered_pin)
                    if "correct" in pin_result:
                        self.pin_verified = True
                    print(pin_result)
                elif choice == "2":
                    print(self.card.eject())
                else:
                    print("Invalid option. try again.")
            else:
           
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Eject Card")
                choice = input("Choose an option: ")
                if choice == "1":
                    print(self.account.check_balance())
                elif choice == "2":
                    try:
                        amount = float(input("Enter the amount: "))
                        result = self.account.deposit(amount)
                        print(result)
                        if "accomplishly" in result:
                            self.offer_receipt("Deposit", amount)
                    except ValueError:
                        print("Invalid input. enter a number.")
                elif choice == "3":
                    try:
                        amount = float(input("Enter the amount: "))
                        result = self.account.withdraw(amount)
                        print(result)
                        if "accomplishly" in result:
                            self.offer_receipt("Withdraw", amount)
                    except ValueError:
                        print("Invalid input. enter a number.")
                elif choice == "4":
                    print(self.card.eject())
                    self.pin_verified = False
                else:
                    print("Invalid option. Try again.")

    def offer_receipt(self, action, amount):
      
        while True:
            choice = input("Do you want a receipt? \nyes: \n no:  ").strip().lower()
            if choice == "yes":
                print(Transaction.receipt(action, amount, self.account.balance))
                break
            elif choice == "no":
                print("Transaction completed -no receipt-")
                break
            else:
                print("Invalid choice. Just type 'yes' or 'no'.")


if __name__ == "__main__":
    atm = ATM()
    atm.start()
