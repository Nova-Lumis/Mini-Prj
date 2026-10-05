# Constructing Bank Account Class
class BankAccount:
    # Takes an owner and initial_balance
    def __init__(self, owner, initial_balance = 0):
        self.owner = owner

        # Initial balance requirement (should be positive)
        self.__validate_initial_balance(initial_balance)
        self.__balance = initial_balance
    
    # A getter 
    @property
    def balance(self):
        return self.__balance

    # displaying balance in the account
    def display_balance(self):
        print(f"{self.owner} account balance: {self.__balance}.\n")
    
    # deposit money to account balance
    def deposit(self, amount):
        # Validate the amount
        self.__validate_amount(amount)

        # deposit main
        self.__balance += amount
        print(f"You have succesfully deposited {amount} to your balance.")
        self.display_balance()
     
    # withdraw money from account balance
    def withdraw(self, amount):
        self.__validate_amount(amount)

        # Amount requirement to withdraw
        if amount > self.__balance:
            raise ValueError("Your withdrawn value is more than your account balance")
        
        # withdraw main
        self.__balance -= amount
        print(f"You have withdrawn {amount} from your account.")
        self.display_balance()
       
    # Validating inputed amount
    def __validate_amount(self, amount):
        # Validating amount data type
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("The amount value should be a number.")
        
        # Validating amount value requirement (must positive number)
        if amount <= 0:
            raise ValueError("The amount deposited/withdrawn should be more than 0.")
    
    # Validating initial balance
    def __validate_initial_balance(self, amount):
        # Initial balance requirement validation, should be a number and amount >= 0.
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("The initial balance value should be a number.")
                
        if amount < 0:
            raise ValueError("Initial balance of the account should be equal or more than zero")
        



# Main
print("\nAccount 2: ")
account_2 = BankAccount("Rudy", 2000)
account_2.display_balance()
account_2.deposit(3000)
account_2.withdraw(4000)

# Trial: inputed withdrawal value
try:
    account_2.withdraw(2000)
except ValueError as e:
    print(f"error: {e}.\n")

# Trial: inputed initial balance
try:
    account_3 = BankAccount("Tom", -10)
except TypeError as e:
    print(f"error: {e}.\n")
except ValueError as e:
    print(f"error: {e}.\n")
