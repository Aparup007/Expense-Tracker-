# **MunimZ** a one stop solution for managing your expense 

**General**

**Overview**  

**MunimZ** ( "Munim Ji" is a Hindi(Indian) pharse; it means Accountant) is a comprehensive platform designed to streamline and enhance users' financial activities. This one-stop solution provides users with tools to manage transactions, set financial goals, monitor investments, check credit scores, and access personalized offers. The application aims to empower users in making informed financial decisions while offering a seamless and user-friendly experienceis.  

**Features**  
i. User Management -  
User Authentication: Users can securely log in and log out of the application.  
Profile Management: Users can update their profiles and manage account information.  

ii. Transaction Management -  
Payment Processing: Users can make online payments using UPI or cards, with transaction logs generated.  
Manual Entry: Users can manually input details for cash transactions outside the app.  

iii. Investment Opportunities -  
Stock Market Access: Users can explore and invest in stocks through integrated portals.  
Bank Portals: Access to various bank portals for investment opportunities.  

iv. Financial Goal Setting - 
Goal Definition: Users can set financial goals, specifying the amount and deadline.  
Progress Tracking: Track progress towards financial goals with updates and notifications.  

v. Exclusive Offers - 
Offer Discovery: Users can explore personalized offers sorted by the app based on financial behavior.  
Claiming Offers: Users can claim offers, and transaction logs are generated.  

vi. Credit Score Monitoring -  
Credit Score Check: Users can check their credit scores directly from the app.  

vii. Reporting and Analysis - 
Consolidated Reports: Users can generate consolidated reports summarizing transactions, goals, and offers.  
Interactive Visualizations: Visual representation of financial data to aid analysis.  

**Usage**  
Users can access the Financial Management App through an intuitive interface. After logging in, they have the flexibility to manage transactions, set financial goals, explore investment opportunities, and monitor their credit score. The application ensures data security and provides valuable insights to help users make informed financial decisions.  



**Project Schema** :

**Language Used**: Python

1.1.**Categories**:

Core Domain: Defines fundamental classes such as Transaction, Payment, CashTransaction, Investment, Goal, Offer, Report, and CreditScore.  
User Domain: Manages user-related functionalities like login, logout, goal setting, credit score checking, transaction recording, investment, and report generation.  
Notification and Reward Domain: Handles notifications and rewards for users.  
App Domain: Represents the main application structure with an App class for managing users.  

1.2.Core Domain:

Functions  
Transaction: Represents a generic transaction with an ID, amount, date, and description.  
Payment: Represents a payment transaction with an additional payment method.  
CashTransaction: Represents a cash transaction, inheriting from Transaction.  
Investment: Represents an investment transaction with an additional investment type.  
Goal: Represents a financial goal with an ID, goal amount, current amount, and deadline.  
Offer: Represents a financial offer with an ID, details, and validity.  
Report: Represents a financial report with an ID, content, and generation date.  
CreditScore: Represents a user's credit score.  

1.3.User Domain:

Functions  
User: Represents a user with an ID, username, password, email, phone, transactions, credit score, goals, reports, notifications, and rewards.    
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

1.4.Notification and Reward Domain:

Functions  
Notification: Represents a notification with a user, message, and date.  
send_notification: Sends a notification to the user.  
Reward: Represents a reward with an ID, details, and expiry date.  
claim_reward: Claims a reward for a user.  

1.5.App Domain:

Fubnctions  
App: Represents the main application with a list of users.  
start_app: Simulates the start of the application.  
shutdown_app: Simulates the shutdown of the application.  


2.**UML Diagrams**

2.a. Use Case Diagram

![uml_usecase](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/UML%20Diagrams/UML%20Use%20Case%20Diagrame.jpg)

2.b. Activity Diagram 

![uml_activity](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/UML%20Diagrams/UML%20Activity%20Diagram.jpg)

2.c. Class Diagram 

![uml_class](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/UML%20Diagrams/UML%20Class%20Diagram.jpg)

3. **Domain Driven Design**
   
![ddd](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/DDD/Domain%20Driven%20Design.jpg)

4. **Metrics**
--in progress : software installation phase--
