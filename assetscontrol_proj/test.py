from app.basicops import BasicOps
import app.transactions as transactions

def main():
    
    basicops = BasicOps()
    account_name = "John Doe"

    try:
        basicops.delete_account(account_name)
    except ValueError as e:
        print(f"Error: {e}")
               
    # Withdwraw some amount from a non-existing account
    try:
        transactions.withdrawInvestment(account_name, 100.0)
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        # Initialize the investment
        initial_investment = 1000.0
        transactions.initalInvestment(account_name, initial_investment)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        # Withdraw some amount
        withdrawal_amount = 200.0
        transactions.withdrawInvestment(account_name, withdrawal_amount)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        # Transfer some amount to another account
        to_account = "Jane Doe"
        transfer_amount = 300.0
        transactions.transferInvestment(account_name, to_account, transfer_amount)
    except ValueError as e:
        print(f"Error: {e}")

    print(f"Account balances after transactions for {account_name}: {basicops.check_balance(account_name)}")
    print(f"Account balances after transactions for {to_account}: {basicops.check_balance(account_name)}")


main()

    
