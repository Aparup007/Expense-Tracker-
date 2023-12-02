# Expense-Tracker-**MunimZ** (Prototype)

**Project Overview**
**MunimZ** ( "Munim Ji" is a Hindi(Indian) pharse; it means Accountant) is a dynamic Expense Management Tool built in python, through this platform user will be able to execute all type of payments from daily purchases to monthly bills and EMIs; it has also options for investimetns, user will have access to sharemarket and different bonds; it captures log of evey actions and prvides a consolidated Summary upon request. Also it caters customize offers to the user to keep them ahead in the market.

**Project Schema** :

**Language Used**: Python

1.a.**Categories**:

Core Domain: Defines fundamental classes such as Transaction, Payment, CashTransaction, Investment, Goal, Offer, Report, and CreditScore.
User Domain: Manages user-related functionalities like login, logout, goal setting, credit score checking, transaction recording, investment, and report generation.
Notification and Reward Domain: Handles notifications and rewards for users.
App Domain: Represents the main application structure with an App class for managing users.

1.a.1.Core Domain:

Functions
Transaction: Represents a generic transaction with an ID, amount, date, and description.
Payment: Represents a payment transaction with an additional payment method.
CashTransaction: Represents a cash transaction, inheriting from Transaction.
Investment: Represents an investment transaction with an additional investment type.
Goal: Represents a financial goal with an ID, goal amount, current amount, and deadline.
Offer: Represents a financial offer with an ID, details, and validity.
Report: Represents a financial report with an ID, content, and generation date.
CreditScore: Represents a user's credit score.

1.a.2.User Domain:

Functions
User: Represents a user with an ID, username, password, email, phone, transactions, credit score, goals, reports, notifications, and rewards.
Functions:
login: Simulates user login.
logout: Simulates user logout.
set_financial_goal: Sets a financial goal for the user.
check_credit_score: Checks and returns the user's credit score.
generate_consolidated_report: Generates a consolidated report for the user.
make_payment: Records a payment transaction for the user.
make_cash_transaction: Records a cash transaction for the user.
make_investment: Records an investment transaction for the user.
notify_user: Notifies the user with a message.
claim_reward: Claims a reward for the user.

1.a.3.Notification and Reward Domain:

Functions
Notification: Represents a notification with a user, message, and date.
send_notification: Sends a notification to the user.
Reward: Represents a reward with an ID, details, and expiry date.
claim_reward: Claims a reward for a user.

1.a.4.App Domain:

Fubnctions
App: Represents the main application with a list of users.
start_app: Simulates the start of the application.
shutdown_app: Simulates the shutdown of the application.

1.b.Usage:

-The user runs the script, creating an instance of the App class  
-Users are created and added to the application  
-User interactions simulate login, goal setting, credit score checking, transactions, investments, report generation, and notifications  
-The application is then shut down

2.**UML Diagrams**

2.a. Use Case Diagram

![uml_usecase](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/UML%20Diagrams/UML%20Use%20Case%20Diagrame.jpg)

2.b. Activity Diagram 

![uml_activity](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/UML%20Diagrams/UML%20Activity%20Diagram.jpg)

2.c. Class Diagram 

![uml_class](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/UML%20Diagrams/UML%20Class%20Diagram.jpg)

3. **Domain Driven Design**
   
![ddd](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/DDD/Domain%20Driven%20Diagram.jpg)

