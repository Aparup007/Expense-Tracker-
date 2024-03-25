# Financial Management System Code Documentation

## Core Domain

### Transaction
Represents a generic financial transaction.

- `transaction_id`: Unique identifier for the transaction.
- `amount`: The amount involved in the transaction.
- `date`: Date of the transaction.
- `description`: A brief description of the transaction.

### Payment
Represents a payment transaction   1233.

- Inherits from Transaction.
- `payment_method`: The method used for the payment.

- `process_payment()`: Prints a message indicating that the payment has been processed.

### CashTransaction
Represents a cash transaction.

- Inherits from Transaction.

- `record_cash_transaction()`: Prints a message indicating that the cash transaction has been recorded.

### Investment
Represents an investment transaction.

- Inherits from Transaction.
- `investment_type`: The type of investment made.

- `perform_investment()`: Prints a message indicating that the investment has been made.

### Goal
Represents a financial goal.

- `goal_id`: Unique identifier for the goal.
- `goal_amount`: The target amount for the goal.
- `current_amount`: The current amount achieved towards the goal.
- `deadline`: The deadline for achieving the goal.

- `update_progress(amount)`: Updates the current amount based on the provided amount.
- `check_goal_completion()`: Checks if the goal has been completed.

### Offer
Represents a financial offer.

- `offer_id`: Unique identifier for the offer.
- `offer_details`: Details of the offer.
- `validity`: The validity period of the offer.

- `claim_offer()`: Prints a message indicating that the offer has been claimed.

### Report
Represents a financial report.

- `report_id`: Unique identifier for the report.
- `content`: The content of the report.
- `generation_date`: Date when the report was generated.

- `generate_report()`: Prints a message indicating that the report has been generated.

### CreditScore
Represents a user's credit score.

- `credit_score`: The credit score of the user.

- `check_credit_score()`: Prints the user's credit score and returns it.

## User Domain

### LoginLogout
Manages user login and logout functionality.

- `user`: Reference to the associated User object.
- `logged_in`: Boolean flag indicating the login status.

- `login()`: Prints a message indicating that the user has logged in.
- `logout()`: Prints a message indicating that the user has logged out.

### User
Represents a user.

- `user_id`: Unique identifier for the user.
- `username`: The username of the user.
- `password`: The password of the user.
- `email`: The email address of the user.
- `phone`: The phone number of the user.
- `transactions`: List to store user's transactions.
- `credit_score`: CreditScore object representing the user's credit score.
- `goals`: List to store user's financial goals.
- `reports`: List to store user's financial reports.
- `notifications`: List to store user's notifications.
- `rewards`: List to store user's claimed rewards.
- `login_logout`: LoginLogout object managing user login/logout.

#### Functions:

- `set_financial_goal(goal_amount, deadline)`: Sets a financial goal for the user.
- `check_credit_score()`: Checks and returns the user's credit score.
- `generate_consolidated_report()`: Generates a consolidated report for the user.
- `make_payment(amount, description, payment_method)`: Records a payment transaction for the user.
- `make_cash_transaction(amount, description)`: Records a cash transaction for the user.
- `make_investment(amount, description, investment_type)`: Records an investment transaction for the user.
- `notify_user(message)`: Notifies the user with a message.
- `claim_reward(reward)`: Claims a reward for the user.

## Notification and Reward Domain

### Notification
Represents a notification.

- `user`: Reference to the associated User object.
- `message`: The content of the notification.
- `date`: Date when the notification was sent.

- `send_notification()`: Prints a message indicating that the notification has been sent.

### Reward
Represents a reward.

- `reward_id`: Unique identifier for the reward.
- `reward_details`: Details of the reward.
- `expiry_date`: Date when the reward expires.

- `claim_reward(user)`: Claims a reward for the user.

## App Domain

### App
Represents the main application.

- `users`: List to store User objects.

#### Functions:

- `start_app()`: Prints a message indicating that the app has started.
- `shutdown_app()`: Prints a message indicating that the app has shutdown.

## Example Usage

```python
if __name__ == "__main__":
    financial_app = App()
    financial_app.start_app()

    # Create a user
    alice = User(user_id=1, username="Alice", password="password123", email="alice@example.com", phone="1234567890")
    financial_app.users.append(alice)

    # User interactions
    alice.login_logout.login()
    alice.set_financial_goal(goal_amount=5000, deadline=datetime(2023, 12, 31))
    alice.check_credit_score()
    alice.make_payment(amount=1000, description="Online purchase", payment_method="Credit Card")
    alice.make_cash_transaction(amount=200, description="Grocery shopping")
    alice.make_investment(amount=3000, description="Stocks", investment_type="Stock Market")
    alice.generate_consolidated_report()

    # Notification and Reward
    alice.notify_user("New offer available!")
    
    reward = Reward(reward_id=1, reward_details="10% discount on next purchase", 
                    expiry_date=datetime.now() + timedelta(days=30))
    alice.claim_reward(reward)

    # User logout
    alice.login_logout.logout()
