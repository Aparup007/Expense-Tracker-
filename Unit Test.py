import unittest
from datetime import datetime
from unittest.mock import patch
from io import StringIO
from Source_Code import (
    User,
    Payment,
    CashTransaction,
    Limit,
    Report,
    LoginLogout,
    App
)

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(
            user_id=1,
            username="test_user",
            password="password",
            email="test@example.com",
            phone="1234567890"
        )

    def test_set_financial_limit(self):
        self.user.set_financial_limit(limit_amount=1000, deadline=datetime.now())
        self.assertEqual(len(self.user.limits), 1)

    def test_generate_consolidated_report(self):
        self.user.set_financial_limit(limit_amount=1000, deadline=datetime.now())
        report = self.user.generate_consolidated_report()
        self.assertEqual(len(self.user.reports), 1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_make_payment(self, mock_stdout):
        self.user.make_payment(amount=50, description="Test payment", payment_method="Credit Card")
        self.assertEqual(len(self.user.transactions), 1)
        self.assertIn("Payment of 50 made via Credit Card.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_make_cash_transaction(self, mock_stdout):
        self.user.make_cash_transaction(amount=50, description="Test cash transaction")
        self.assertEqual(len(self.user.transactions), 1)
        self.assertIn("Cash transaction of 50 recorded.", mock_stdout.getvalue())

class TestPayment(unittest.TestCase):
    def test_process_payment(self):
        payment = Payment(
            transaction_id=1,
            amount=100,
            date=datetime.now(),
            description="Test payment",
            payment_method="Credit Card"
        )
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            payment.process_payment()
            self.assertIn("Payment processed via Credit Card.", mock_stdout.getvalue())

class TestCashTransaction(unittest.TestCase):
    def test_record_cash_transaction(self):
        cash_transaction = CashTransaction(
            transaction_id=1,
            amount=100,
            date=datetime.now(),
            description="Test cash transaction"
        )
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            cash_transaction.record_cash_transaction()
            self.assertIn("Cash transaction recorded.", mock_stdout.getvalue())

class TestLimit(unittest.TestCase):
    def test_update_spending(self):
        limit = Limit(limit_id=1, limit_amount=1000, deadline=datetime.now())
        limit.update_spending(amount=500)
        self.assertEqual(limit.current_amount, 500)

    def test_check_limit_exceeded(self):
        limit = Limit(limit_id=1, limit_amount=1000, deadline=datetime.now())
        limit.update_spending(amount=1500)
        self.assertTrue(limit.check_limit_exceeded())

class TestReport(unittest.TestCase):
    def test_generate_report(self):
        report = Report(report_id=1, content="Test report", generation_date=datetime.now())
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            report.generate_report()
            self.assertIn("Report generated on", mock_stdout.getvalue())

class TestLoginLogout(unittest.TestCase):
    def test_login(self):
        user = User(
            user_id=1,
            username="test_user",
            password="password",
            email="test@example.com",
            phone="1234567890"
        )
        login_logout = LoginLogout(user)
        login_logout.login()
        self.assertTrue(login_logout.logged_in)

    def test_logout(self):
        user = User(
            user_id=1,
            username="test_user",
            password="password",
            email="test@example.com",
            phone="1234567890"
        )
        login_logout = LoginLogout(user)
        login_logout.logged_in = True
        login_logout.logout()
        self.assertFalse(login_logout.logged_in)

class TestApp(unittest.TestCase):
    def test_start_app(self):
        app = App()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            app.start_app()
            self.assertIn("App started.", mock_stdout.getvalue())

    def test_shutdown_app(self):
        app = App()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            app.shutdown_app()
            self.assertIn("App shutdown.", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
