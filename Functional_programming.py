#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
from typing import List

# Core Domain

class Transaction:
    def __init__(self, transaction_id: int, amount: float, date: datetime, description: str):
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = date
        self.description = description

class Payment(Transaction):
    def __init__(self, transaction_id: int, amount: float, date: datetime, description: str, payment_method: str):
        super().__init__(transaction_id, amount, date, description)
        self.payment_method = payment_method

    def process_payment(self) -> str:
        return f"Payment processed via {self.payment_method}."

class CashTransaction(Transaction):
    def __init__(self, transaction_id: int, amount: float, date: datetime, description: str):
        super().__init__(transaction_id, amount, date, description)

    def record_cash_transaction(self) -> str:
        return "Cash transaction recorded."

class Investment(Transaction):
    def __init__(self, transaction_id: int, amount: float, date: datetime, description: str, investment_type: str):
        super().__init__(transaction_id, amount, date, description)
        self.investment_type = investment_type

    def perform_investment(self) -> str:
        return f"Investment made in {self.investment_type}."

class Goal:
    def __init__(self, goal_id: int, goal_amount: float, deadline: datetime):
        self.goal_id = goal_id
        self.goal_amount = goal_amount
        self.current_amount = 0
        self.deadline = deadline

    def update_progress(self, amount: float) -> None:
        self.current_amount += amount

    def check_goal_completion(self) -> bool:
        return self.current_amount >= self.goal_amount

# User Domain

class CreditScore:
    def __init__(self, credit_score: int):
        self.credit_score = credit_score

    def check_credit_score(self) -> int:
        return self.credit_score

class LoginLogout:
    def __init__(self, user):
        self.user = user
        self.logged_in = False

    def login(self) -> str:
        self.logged_in = True
        return f"User {self.user.username} logged in."

    def logout(self) -> str:
        self.logged_in = False
        return f"User {self.user.username} logged out."

class User:
    def __init__(self, user_id: int, username: str, password: str, email: str, phone: str):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.transactions: List[Transaction] = []
        self.credit_score = CreditScore(700)  # Default credit score
        self.goals: List[Goal] = []
        self.reports: List['Report'] = []  # Forward reference for Report
        self.notifications: List['Notification'] = []
        self.rewards: List['Reward'] = []
        self.login_logout = LoginLogout(self)

    def set_financial_goal(self, goal_amount: float, deadline: datetime) -> None:
        goal = Goal(len(self.goals) + 1, goal_amount, deadline)
        self.goals.append(goal)
        print(f"Financial goal set: {goal_amount} by {deadline}.")

    def generate_consolidated_report(self) -> 'Report':  # Forward reference for Report
        report_content = f"Consolidated Report for {self.username}:\n"
        for goal in self.goals:
            report_content += f"Goal {goal.goal_id}: {goal.current_amount}/{goal.goal_amount} achieved.\n"
        report = Report(len(self.reports) + 1, report_content, datetime.now())
        self.reports.append(report)
        print("Consolidated report generated.")
        return report

    def make_payment(self, amount: float, description: str, payment_method: str) -> Transaction:
        transaction = Payment(len(self.transactions) + 1, amount, datetime.now(), description, payment_method)
        self.transactions.append(transaction)
        print(f"Payment of {amount} made via {payment_method}.")
        return transaction

    def make_cash_transaction(self, amount: float, description: str) -> Transaction:
        transaction = CashTransaction(len(self.transactions) + 1, amount, datetime.now(), description)
        self.transactions.append(transaction)
        print(f"Cash transaction of {amount} recorded.")
        return transaction

    def make_investment(self, amount: float, description: str, investment_type: str) -> Transaction:
        transaction = Investment(len(self.transactions) + 1, amount, datetime.now(), description, investment_type)
        self.transactions.append(transaction)
        print(f"Investment of {amount} made in {investment_type}.")
        return transaction

    def notify_user(self, message: str) -> None:
        notification = Notification(user=self, message=message, date=datetime.now())
        self.notifications.append(notification)
        notification.send_notification()

    def claim_reward(self, reward: 'Reward') -> None:  # Forward reference for Reward
        reward.claim_reward(self)

# Notification and Reward Domain

class Notification:
    def __init__(self, user: User, message: str, date: datetime):
        self.user = user
        self.message = message
        self.date = date

    def send_notification(self) -> str:
        return f"Notification to {self.user.username} on {self.date}: {self.message}"

class Reward:
    def __init__(self, reward_id: int, reward_details: str, expiry_date: datetime):
        self.reward_id = reward_id
        self.reward_details = reward_details
        self.expiry_date = expiry_date

    def claim_reward(self, user: User) -> str:
        return f"Reward claimed by {user.username}: {self.reward_details}"

# App Domain

class App:
    def __init__(self):
        self.users: List[User] = []

    def start_app(self) -> str:
        return "App started."

    def shutdown_app(self) -> str:
        return "App shutdown."

