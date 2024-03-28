from datetime import datetime

# Define the Payment, CashTransaction, and Investment classes here
class Payment:
    def __init__(self, transaction_id, amount, date, description, payment_method):
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = date
        self.description = description
        self.payment_method = payment_method

class CashTransaction:
    def __init__(self, transaction_id, amount, date, description):
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = date
        self.description = description

class Investment:
    def __init__(self, transaction_id, amount, date, description, investment_type):
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = date
        self.description = description
        self.investment_type = investment_type

class DSLTransaction:
    def __init__(self):
        self.transactions = []

    def payment(self, amount: float, description: str, payment_method: str):
        transaction = Payment(len(self.transactions) + 1, amount, datetime.now(), description, payment_method)
        self.transactions.append(transaction)
        return transaction

    def cash_transaction(self, amount: float, description: str):
        transaction = CashTransaction(len(self.transactions) + 1, amount, datetime.now(), description)
        self.transactions.append(transaction)
        return transaction

    def investment(self, amount: float, description: str, investment_type: str):
        transaction = Investment(len(self.transactions) + 1, amount, datetime.now(), description, investment_type)
        self.transactions.append(transaction)
        return transaction

# Example usage of the DSL
dsl = DSLTransaction()

# Using the DSL to create transactions
dsl.payment(100, "Shopping", "Credit Card")
dsl.cash_transaction(50, "Lunch")
dsl.investment(500, "Stocks", "Technology")

# Accessing the transactions created using DSL
for transaction in dsl.transactions:
    print(transaction.__class__.__name__, ":", transaction.description)
