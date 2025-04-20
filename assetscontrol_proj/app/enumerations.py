class Enumerations:
    """
    This class contains enumerations for various types of data.
    """

    class Transaction_Type:
        """
        This class contains enumerations for different types of operations.
        """
        DEBIT = "debit"
        CREDIT = "credit"
    
    class Operation_Type:
        """
        This class contains enumerations for different types of operations.
        """
        ADD = "add"
        SUBTRACT = "subtract"
        ZEROING = "zero"

    class Transaction_Details:
        """
        This class contains enumerations for different types of transaction details.
        """
        INITIAL_INVESTMENT = "Initial Investment"
        DIVIDEND = "Dividend"
        INTEREST = "Interest"
        LOAN = "Loan"
        WITHDRAWAL = "Withdrawal"
        REINVESTMENT = "Reinvestment"
        SALE = "Sale"
        TRANSFER_IN = "Transfer In To: "
        TRANSFER_OUT = "Transfer Out From: "