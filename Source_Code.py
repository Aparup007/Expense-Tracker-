from datetime import datetime

# Core Domain

class Transaction:
    def __init__(self, transaction_id, amount, date, description):
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = date
        self.description = description


class Payment(Transaction):
    def __init__(self, transaction_id, amount, date, description, payment_method):
        super().__init__(transaction_id, amount, date, description)
        self.payment_method = payment_method

    def process_payment(self):
        print(f"Payment processed via {self.payment_method}.")


class CashTransaction(Transaction):
    def __init__(self, transaction_id, amount, date, description):
        super().__init__(transaction_id, amount, date, description)

    def record_cash_transaction(self):
        print(f"Cash transaction recorded.")


class Limit:
    def __init__(self, limit_id, limit_amount, deadline):
        self.limit_id = limit_id
        self.limit_amount = limit_amount
        self.current_amount = 0
        self.deadline = deadline

    def update_spending(self, amount):
        self.current_amount += amount

    def check_limit_exceeded(self):
        return self.current_amount > self.limit_amount


class Report:
    def __init__(self, report_id, content, generation_date):
        self.report_id = report_id
        self.content = content
        self.generation_date = generation_date

    def generate_report(self):
        print(f"Report generated on {self.generation_date}:\n{self.content}")


# User Domain

class LoginLogout:
    def __init__(self, user):
        self.user = user
        self.logged_in = False

    def login(self):
        self.logged_in = True
        print(f"User {self.user.username} logged in.")

    def logout(self):
        self.logged_in = False
        print(f"User {self.user.username} logged out.")

class User:
    def __init__(self, user_id, username, password, email, phone):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.transactions = []
        self.limits = []
        self.reports = []
        self.login_logout = LoginLogout(self)

    def set_financial_limit(self, limit_amount, deadline):
        limit = Limit(len(self.limits) + 1, limit_amount, deadline)
        self.limits.append(limit)
        print(f"Financial limit set: {limit_amount} by {deadline}.")

    def generate_consolidated_report(self):
        report_content = f"Consolidated Report for {self.username}:\n"
        for limit in self.limits:
            report_content += f"Limit {limit.limit_id}: {limit.current_amount}/{limit.limit_amount} spent.\n"
        report = Report(len(self.reports) + 1, report_content, datetime.now())
        self.reports.append(report)
        print("Consolidated report generated.")
        return report

    def make_payment(self, amount, description, payment_method):
        transaction = Payment(len(self.transactions) + 1, amount, datetime.now(), description, payment_method)
        self.transactions.append(transaction)
        print(f"Payment of {amount} made via {payment_method}.")

    def make_cash_transaction(self, amount, description):
        transaction = CashTransaction(len(self.transactions) + 1, amount, datetime.now(), description)
        self.transactions.append(transaction)
        print(f"Cash transaction of {amount} recorded.")

    def notify_user(self, message):
        notification = Notification(user=self, message=message, date=datetime.now())
        self.notifications.append(notification)
        notification.send_notification()

# Notification Domain

class Notification:
    def __init__(self, user, message, date):
        self.user = user
        self.message = message
        self.date = date

    def send_notification(self):
        print(f"Notification to {self.user.username} on {self.date}: {self.message}")

# App Domain

class App:
    def __init__(self):
        self.users = []

    def start_app(self):
        print("App Started.")

    def shutdown_app(self):
        print("App Shutdown.")
