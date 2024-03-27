import unittest
from datetime import datetime, timedelta
from Source_Code import User, Payment, CashTransaction, Investment, Goal, Report, CreditScore, Notification, Reward

class TestUser(unittest.TestCase):
    def setUp(self):
        # Create a dummy user for testing
        self.user = User(1, "test_user", "password123", "test@example.com", "1234567890")

    def test_set_financial_goal(self):
        # Test setting a financial goal
        self.user.set_financial_goal(1000, datetime.now() + timedelta(days=30))
        self.assertEqual(len(self.user.goals), 1)  # Check if a goal is added
        self.assertEqual(self.user.goals[0].goal_amount, 1000)  # Check the goal amount

    def test_make_payment(self):
        # Test making a payment
        initial_transactions_count = len(self.user.transactions)
        self.user.make_payment(50, "Test payment", "Credit Card")
        self.assertEqual(len(self.user.transactions), initial_transactions_count + 1)  # Check if a transaction is added
        self.assertIsInstance(self.user.transactions[-1], Payment)  # Check if the transaction type is Payment

    def test_make_cash_transaction(self):
        # Test making a cash transaction
        initial_transactions_count = len(self.user.transactions)
        self.user.make_cash_transaction(20, "Test cash transaction")
        self.assertEqual(len(self.user.transactions), initial_transactions_count + 1)  # Check if a transaction is added
        self.assertIsInstance(self.user.transactions[-1], CashTransaction)  # Check if the transaction type is CashTransaction

    # Add more test methods for other User class methods if needed

if __name__ == '__main__':
    unittest.main()
