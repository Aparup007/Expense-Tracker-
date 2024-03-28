## General

### Overview 

**MunimZ** ( "Munim Ji" is a Hindi(Indian) pharse; it means Accountant) is a comprehensive platform designed to streamline and enhance users' financial activities. This one-stop solution provides users with tools to manage transactions, set financial goals, monitor investments, check credit scores, and access personalized offers. The application aims to empower users in making informed financial decisions while offering a seamless and user-friendly experienceis.  

### Features
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

### Usage
Users can access the Financial Management App through an intuitive interface. After logging in, they have the flexibility to manage transactions, set financial goals, explore investment opportunities, and monitor their credit score. The application ensures data security and provides valuable insights to help users make informed financial decisions.  

## 1. Git
A few years ago, I used GitHub, so going back to it recently was like a good refresher session for me. It made me better at excuting git actions like colne, push, pull, commit etc. . Git also helped me easily connect my project with other tools I used in my project, like SonarCloud, Maven, and Jenkins. Overall, working with Git for this assigment was a fun experience ! 

## 2. UML Diagrams
For my project I have used below three UML diagrams: 

1. [Activity Diagram: ](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/UML%20Diagrams/UML%20User%20Activity%20Diagram.png): This Activity Diagram shows the end to end workflow of the system
2. [Class Diagram: ](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/UML%20Diagrams/UML%20Class%20Diagram.png): The Class Diagram illustrates various classes written for the system and their relationships.
3. [Use Case Diagram: ](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/UML%20Diagrams/UML%20Use%20Case%20Diagram.png): This Use Case Diagram shows that interaction between user and diffrent functionlities of the system

## 3. DDD
I have design [Context Mapping Diagram](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/DDD/Contex%20Mapping%20Diagram.png), [Core Domain Chart](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/DDD/Core%20Diagram%20Chart.jpg) and [Event storming diagram](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/DDD/Event%20storming%20diagram.png) which compliments the entire systme architecture

## 4. Metrics
![sonar_cube](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/miscellaneous/sonarcloud%20logo.png)                                                                                                  
SonarCloud has been used for analyse code quality
Below are the metrics and correposding results                                                                                                                                                                                                                                                                                                                                                                                                             
![sonar_cloud](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/miscellaneous/SonarCloud%20result.png)
![code_passed](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/miscellaneous/Code_passed.png)


## 5. Clean Code Developement
Below are the 5 methods with example among the many which has been used to write clean code for the project

1. Descriptive Variable Names: In the code, variable names like user_id, username, amount, etc., are descriptive and convey the purpose of the variable. This makes the code easier to understand for anyone reading it.
2. Modularization: The code is divided into meaningful classes such as User, Transaction, Payment, etc., each responsible for a specific aspect of the system. This modularization enhances code organization and 
   maintainability.
3. Encapsulation:	Encapsulation is maintained by using private attributes and providing public methods to interact with those attributes. For example, the User class encapsulates user data and provides methods like 
   make_payment(), set_financial_goal(), etc., to interact with it.
4. Code Reusability: By defining classes and methods with clear responsibilities, the code promotes reuse. For instance, the Payment class can be reused for different payment methods, and the CashTransaction class can be 
   used for any cash-related transactions.
5. Error Handling: Although not explicitly shown in the provided code, error handling is an essential aspect of clean code. Implementing proper error handling mechanisms ensures that the code behaves predictably and 
   gracefully handles unexpected situations, enhancing robustness and reliability.

Here is my personal CCD [cheatsheet](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/CCD%20Cheet%20sheet.pdf)

## 6/7. Build/Contimous Delivery :
![jenkins](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/miscellaneous/Screenshot%202024-03-27%20175206.png)                                                                                         
I have installed Jenkins for CI/CD pipeline and used Maven plug-in thorugh Jenkins platform for build process.
This is the screeshot after completing the [build stage](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/miscellaneous/Screenshot%202024-02-21%20185709.png)
I have build the complete CI/CD pipeline in Jenkins                                                                                                                                                                          
                                                                                                                                                                                                                                       
![pipeline](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/miscellaneous/Screenshot%202024-02-28%20163309.png)

## 8. Unit Test: 
I have writtten three unit test case using asserting method to test the code 

1. test_set_financial_goal: This method tests the set_financial_goal method of the User class, verifying if a financial goal is correctly added to the user's goals list.
2. test_make_payment: This method tests the make_payment method of the User class, ensuring that a payment transaction is properly added to the user's transactions list.
3. test_make_cash_transaction: This method tests the make_cash_transaction method of the User class, verifying if a cash transaction is correctly added to the user's transactions list.

This is the [unt test file](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/Unit_test.py)                                                                                                                  
![test_result](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/miscellaneous/Screenshot%202024-02-28%20155057.png)                                                                                  


## 9. IDE:

I have recently started using VS Code for my project, and it is been a great learning experience. Before this, I had not used this platform for coding, so it is been new for me. I must say, I am really impressed with its functionality. The tool is excellent! The plugin options are amazing, and integrating Git repositories is very easy. 
Apart from the common shortcuts, I have also learned some handy ones while working on the project, like,
Ctrl + P: Quick open file
Shift + Alt + F: Format code
Ctrl + `: Show/hide terminal
F5: Start debugging


## 10. DSL:
         
The DSL file is related to the the project only. In this [DSL](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/DSL.py) example, I created a DSLTransaction class that provides methods like payment, cash_transaction, and investment to create different types of financial transactions.

## 11. Functional Programming: 

To cover the mentioned aspects of Functional Programming I have modfiyed the source code accordinly , though this will be considered as out of the core project scope.
Below is the explation of the functional programming,

1. Side-Effect-Free Functions: Methods like process_payment(), record_cash_transaction(), and others now return strings instead of directly printing to the console. This makes the functions side-effect-free, allowing 
   the caller to decide how to handle the returned value.
2. Higher-Order Functions: While the code doesn't significantly use higher-order functions, we can introduce them in future modifications where appropriate. Higher-order functions can be functions like map(), filter(), 
   or functions that take other functions as arguments.
3. Functions as Parameters and Return Values: Functions like send_notification() now return values instead of printing directly. This allows for flexibility and potential use as return values from other functions.
4. Use of Closures / Anonymous Functions: There are no explicit closures or anonymous functions introduced in this version of the code. However, they can be utilized in more advanced scenarios to encapsulate behavior 
   within functions.
   




                                                                                                                                                                                                                        
                                                                                                                                                                                                                        
                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                       




