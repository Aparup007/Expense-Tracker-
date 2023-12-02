# Expense-Tracker-**MunimZ** (Prototype)
**MunimZ** ( "Munim Ji" is a Hindi pharse; it means Accountant) is a dynamic Expense Tracker built with python, it will help to track your Daily Expenses and prvide you a Summary and keep you safe from moth-end dilemma \\m//
![uml_activity](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/UML%20Diagrams/UML%20Activity%20Diagram.jpg)
![uml_class](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/UML%20Diagrams/UML%20Class%20Diagram.jpg)
![uml_usecase](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/UML%20Diagrams/UML%20Use%20Case%20Diagrame.jpg)
![[ddd](https://github.com/Aparup007/One-Stop-Expense-Solution-MunimZ/blob/main/DDD/Domain%20Driven%20Diagram.jpg)
**Project Overview** : 
MunimZ is a Python program that allows users to manage and track their expenses. Users can add, view, delete, and summarize expenses based on different categories, such as food, transportation, rent, etc. The program uses a Dictionary to organize expenses by category and stores the data persistently using the pickle module.

**Project Schema** :
The project consists of a single Python script, and the core functionality is divided into diffrenrt functions blocks. 
    Main Components : 
    Data Storage: The program uses a Dictionary  to store expense data. Each category is a key in the Dictionary, and the associated value is a List of expenses in that category.
    Data Persistence: The pickle module is used to save and load the Dictionary from .pkl file. /n
    User Interface: The program offers a menu-driven command-line interface to interact with the expense tracker. Users can choose from the following options:
    Add an Expense 
    View Expenses 
    Delete an Expense 
    View Expense Summary 
    Exit 

Functions Written  : 
load_expenses() : Loads the existing expense data from the "expenses.pkl" file into the expenses dictionary when the program starts.
save_expenses() : Saves the current expenses dictionary to the "expenses.pkl" file. 
show_menu() : Displays the main menu options for the user to choose from.
add_expense() : Allows the user to add a new expense.
view_expenses() :  Displays the list of expenses categorized by their respective categories.
delete_expense() : Allows the user to delete an expense from a specific category.
view_summary() : Provides an expense summary that shows the total expenses for each category and the overall total.

Usage :
>Run the script in a Python environment.
>Follow the on-screen menu to add, view, delete, or summarize expenses.
>When done, select the "Exit" option to save the data and exit the program.

Conclusion :
"MunimZ" is a simple and effective tool for managing personal expenses. Users can easily keep track of their spending in different categories, view summaries, and continue managing their expenses across multiple sessions.
