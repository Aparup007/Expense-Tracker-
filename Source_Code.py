from datetime import datetime, timedelta

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


class Investment(Transaction):
    def __init__(self, transaction_id, amount, date, description, investment_type):
        super().__init__(transaction_id, amount, date, description)
        self.investment_type = investment_type

    def perform_investment(self):
        print(f"Investment made in {self.investment_type}.")


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


class Offer:
    def __init__(self, offer_id, offer_details, validity):
        self.offer_id = offer_id
        self.offer_details = offer_details
        self.validity = validity

    def claim_offer(self):
        print(f"Offer claimed: {self.offer_details}.")


class Report:
    def __init__(self, report_id, content, generation_date):
        self.report_id = report_id
        self.content = content
        self.generation_date = generation_date

    def generate_report(self):
        print(f"Report generated on {self.generation_date}:\n{self.content}")


class CreditScore:
    def __init__(self, credit_score):
        self.credit_score = credit_score

    def check_credit_score(self):
        print(f"Credit Score: {self.credit_score}")
        return self.credit_score


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
        self.credit_score = CreditScore(700)  # Default credit score
        self.goals = []
        self.reports = []
        self.notifications = []
        self.rewards = []
        self.login_logout = LoginLogout(self)

    def set_financial_goal(self, goal_amount, deadline):
        goal = Goal(len(self.goals) + 1, goal_amount, deadline)
        self.goals.append(goal)
        print(f"Financial goal set: {goal_amount} by {deadline}.")

    def check_credit_score(self):
        return self.credit_score.check_credit_score()

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

    def make_investment(self, amount, description, investment_type):
        transaction = Investment(len(self.transactions) + 1, amount, datetime.now(), description, investment_type)
        self.transactions.append(transaction)
        print(f"Investment of {amount} made in {investment_type}.")

    def notify_user(self, message):
        notification = Notification(user=self, message=message, date=datetime.now())
        self.notifications.append(notification)
        notification.send_notification()

    def claim_reward(self, reward):
        reward.claim_reward(self)

# Notification and Reward Domain

class Notification:
    def __init__(self, user, message, date):
        self.user = user
        self.message = message
        self.date = date

    def send_notification(self):
        print(f"Notification to {self.user.username} on {self.date}: {self.message}")

class Reward:
    def __init__(self, reward_id, reward_details, expiry_date):
        self.reward_id = reward_id
        self.reward_details = reward_details
        self.expiry_date = expiry_date

    def claim_reward(self, user):
        print(f"Reward claimed by {user.username}: {self.reward_details}")

# App Domain

class App:
    def __init__(self):
        self.users = []

    def start_app(self):
        print("App started.")

    def shutdown_app(self):
        print("App shutdown.")
