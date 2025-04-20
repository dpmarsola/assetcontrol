from app.properties import Properties
from app.enumerations import Enumerations
import sqlite3

class BasicOps:

    __properties = None

    def __init__(self):
        self.__properties = Properties().read_properties()


    def debit_account(self, account_name, transaction_detail, amount):
        self.__update_balance(account_name, amount, Enumerations.Operation_Type.SUBTRACT)
        self.__write_new_transaction(account_name, amount, transaction_detail, Enumerations.Transaction_Type.DEBIT)


    def credit_account(self, account_name, transaction_detail, amount):
        
        acctbalance = self.check_balance(account_name)
        
        if acctbalance is None:
            self.__insert_account(account_name, amount)
        else:
            self.__update_balance(account_name, amount, Enumerations.Operation_Type.ADD)

        self.__write_new_transaction(account_name, amount, transaction_detail, Enumerations.Transaction_Type.CREDIT)
        
        
    def check_balance(self, account_name):
        conn = sqlite3.connect(self.__properties["database.name"])
        cursor = conn.cursor()

        # Check if the account exists
        result = cursor.execute("SELECT name, balance FROM accounts WHERE name = ?", (account_name,)).fetchone()

        if result is None:
            return None
        else:
            return result[1]


    def __insert_account(self, account_name, amount):
        conn = sqlite3.connect(self.__properties["database.name"])
        cursor = conn.cursor()

        # Insert the new account with the initial balance
        cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (account_name, amount))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        
        
    def __update_balance(self, account_name, amount, operation):
        conn = sqlite3.connect(self.__properties["database.name"])
        cursor = conn.cursor()

        if operation == Enumerations.Operation_Type.ADD:
            cursor.execute("UPDATE accounts SET balance = balance + ? WHERE name = ?", (amount, account_name))
        elif operation == Enumerations.Operation_Type.SUBTRACT:
            cursor.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, account_name))
        elif operation == Enumerations.Operation_Type.ZEROING:
            cursor.execute("UPDATE accounts SET balance = 0 WHERE name = ?", (account_name,))

        conn.commit()
        conn.close()

    def __write_new_transaction(self, account_name, amount, transaction_detail, transaction_type):
        conn = sqlite3.connect(self.__properties["database.name"])
        cursor = conn.cursor()

        currentdatetime = cursor.execute("SELECT datetime('now')").fetchone()[0]

        account_id = cursor.execute("SELECT id FROM accounts WHERE name = ?", (account_name,)).fetchone()[0]
          
        cursor.execute("INSERT INTO transactions (account_id, amount, transaction_detail, transaction_type, transaction_date) VALUES (?, ?, ?, ?, ?)",
                       (account_id, amount, transaction_detail, transaction_type, currentdatetime))
        
        conn.commit()
        conn.close()
        
    def delete_account(self, account_name):
        conn = sqlite3.connect(self.__properties["database.name"])
        cursor = conn.cursor()

        # Delete the account and its transactions
        cursor.execute("DELETE FROM transactions WHERE account_id = (SELECT id FROM accounts WHERE name = ?)", (account_name,))
        cursor.execute("DELETE FROM accounts WHERE name = ?", (account_name,))

        conn.commit()
        conn.close()

