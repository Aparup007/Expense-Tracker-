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


class Goal:
    def __init__(self, goal_id, goal_amount, deadline):
        self.goal_id = goal_id
        self.goal_amount = goal_amount
        self.current_amount = 0
        self.deadline = deadline

    def update_progress(self, amount):
        self.current_amount += amount

    def check_goal_completion(self):
        return self.current_amount >= self.goal_amount


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
        self.goals = []
        self.reports = []
        self.login_logout = LoginLogout(self)

    def set_financial_goal(self, goal_amount, deadline):
        goal = Goal(len(self.goals) + 1, goal_amount, deadline)
        self.goals.append(goal)
        print(f"Financial goal set: {goal_amount} by {deadline}.")

    def generate_consolidated_report(self):
        report_content = f"Consolidated Report for {self.username}:\n"
        for goal in self.goals:
            report_content += f"Goal {goal.goal_id}: {goal.current_amount}/{goal.goal_amount} achieved.\n"
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

# App Domain

class App:
    def __init__(self):
        self.users = []

    def start_app(self):
        print("App started.")

    def shutdown_app(self):
        print("App shutdown.")

# Example Usage
if __name__ == "__main__":
    financial_app = App()
    financial_app.start_app()

    # Create a user
    alice = User(user_id=1, username="Alice", password="password123", email="alice@example.com", phone="1234567890")
    financial_app.users.append(alice)

    # User interactions
    alice.login_logout.login()
    alice.set_financial_goal(goal_amount=5000, deadline=datetime(2023, 12, 31))
    alice.make_payment(amount=1000, description="Online purchase", payment_method="Credit Card")
    alice.make_cash_transaction(amount=200, description="Grocery shopping")
    alice.generate_consolidated_report()

    # User logout
    alice.login_logout.logout()
