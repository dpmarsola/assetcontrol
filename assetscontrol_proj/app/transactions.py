from app.basicops import BasicOps
from app.enumerations import Enumerations

def initalInvestment(account_name, amount):
    """
    This function initializes the investment process.
    It sets up the necessary parameters and configurations for the investment.
    """

    basicops = BasicOps()
    
    current_balance = basicops.check_balance(account_name)
    if current_balance is None:
        basicops.credit_account(account_name, Enumerations.Transaction_Details.INITIAL_INVESTMENT, amount)
    else:
        raise ValueError(f"Account {account_name} already exists with balance: {current_balance}. Cannot initialize investment.")


def withdrawInvestment(account_name, amount):
    """
    This function withdraws the investment amount from the account.
    It updates the account balance and records the transaction.
    """

    basicops = BasicOps()
    current_balance = basicops.check_balance(account_name)
    if current_balance is None:
        raise ValueError(f"Account {account_name} does not exist.")
    elif current_balance < amount:
        raise ValueError(f"Insufficient funds in account {account_name}. Current balance: {current_balance}, Withdrawal amount: {amount}")
    else:
        basicops.debit_account(account_name, Enumerations.Transaction_Details.WITHDRAWAL, amount)

def transferInvestment(from_account, to_account, amount):
    """
    This function transfers the investment amount from one account to another.
    It updates the balances of both accounts and records the transaction.
    """
    basicops = BasicOps()
    
    from_balance = basicops.check_balance(from_account)
    if from_balance is None:
        raise ValueError(f"Account {from_account} does not exist.")
    elif from_balance < amount:
        raise ValueError(f"Insufficient funds in account {from_account}. Current balance: {from_balance}, Transfer amount: {amount}")
    else:
        transaction_detail = f'{Enumerations.Transaction_Details.TRANSFER_OUT} {from_account} {Enumerations.Transaction_Details.TRANSFER_IN} {to_account}'
        basicops.debit_account(from_account, transaction_detail, amount)
        basicops.credit_account(to_account, transaction_detail, amount)
