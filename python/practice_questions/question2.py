# Creating a class
class BankAccount:
    # Constructor method, where balance has a default value of 0
    def __init__(self, accountNumber, balance=0) -> None:
        # Initializing values
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount):
        """
        deposits the amount provided into the account object. i.e. increments the amount

        Arguments:
        amount : float : the amount to deposit

        Returns:
        None
        """
        self.balance += amount
        print(f"The amount of ${amount} is successfully deposited.")
    
    def withdraw(self, amount):
        """
        withdraws the amount provided from the account object. i.e. decrements the amount from balance if the balance is sufficient, else prints 'Insufficient balance'

        Arguments:
        amount : float : the amount to withdraw

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient Funds !!")
        else:
            self.balance -= amount
            print(f"Withdraw of ${amount} successful !")
    
    def get_balance(self):
        """
        displays the balance in the account object

        Arguments:
        None

        Returns:
        None
        """
        print(f"The current balance of account {self.accountNumber} is ${self.balance}.")

# The main code
if __name__ == "__main__":
    # Creating an object of the class
    my_account = BankAccount(32456960012, 4500)
    # Performing operations to the class object
    my_account.get_balance()
    my_account.deposit(300)
    my_account.get_balance()
    my_account.withdraw(5000)
    my_account.withdraw(4000)
    my_account.get_balance()

    print("\n\n")
    # Creating an object of the class with default balance
    another_account = BankAccount(45678900122)
    # Performing operations to the class object
    my_account.get_balance()
    my_account.withdraw(100)
    my_account.deposit(1000)
    my_account.get_balance()
    my_account.withdraw(100)
    my_account.get_balance()