class BankAccount:
    """
    A simple bank account class that demonstrates OOP concepts.
    
    This class encapsulates banking operations including deposits, withdrawals,
    and balance inquiries while maintaining data integrity.
    """
    
    def __init__(self, initial_balance=0):
        """
        Initialize a new bank account.
        
        Args:
            initial_balance (float): Starting balance for the account. Defaults to 0.
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Add money to the account.
        
        Args:
            amount (float): Amount to deposit. Must be positive.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.
        
        Args:
            amount (float): Amount to withdraw.
            
        Returns:
            bool: True if withdrawal was successful, False if insufficient funds.
        """
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
