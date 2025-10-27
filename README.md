# Python Projects

This repository contains a collection of Python projects that demonstrate concepts such as file handling, data validation, error handling, and user interaction.

---

## Book List Tracker
A Python program that allows users to add, view, search, and delete books stored in a CSV file.  
It demonstrates the use of file handling, data validation, and basic CRUD operations.

### Features
- Add books with title, author, and description  
- Prevent duplicate entries  
- Search for books by title  
- Delete books from the list  
- Automatically creates a CSV file if none exists  

### How to Run
```
python BOOK LIST.py
```

### Concepts Used
- CSV file handling  
- Loops and conditionals  
- Exception handling  
- Input validation  

---

## Expense Tracker
A command-line application that tracks and summarizes weekly expenses.  
It calculates totals, averages, and identifies the days with the highest and lowest expenses.

### Features
- Enter daily expenses for each day of the week  
- Calculates total and average weekly expenses  
- Displays the highest and lowest spending days  
- Validates user input and prevents invalid entries  
- Allows multiple weeks of tracking  

### How to Run
```
python EXPENSE TRACKER.py
```

### Concepts Used
- Lists and loops  
- Exception handling  
- Input validation  
- Basic mathematical operations  

---

## Weekly Recipe Planner
A Python program that manages recipes, ingredients, and user meal plans.  
It allows users to register, log in, create and edit recipes, plan meals for the week, and generate shopping lists automatically from their planned meals.

### Features
- Add, edit, view, and delete recipes  
- Store ingredients with quantities and units for each recipe  
- User registration and login system  
- Weekly meal planning for each user  
- Generate a shopping list based on planned meals  
- Search recipes by name or ingredient  
- Save and load data from CSV files  

### How to Run
```
python recipe_planner.py
```

### Files Used
- PROCESS.CSV: Stores recipe details (ID, name, cuisine, serves, and process)  
- INGREDIENTS.CSV: Stores ingredients linked to each recipe  
- users.csv: Stores user credentials and their weekly meal plans  

*These CSV files will be created automatically when you run the program for the first time if they do not already exist.*

### Concepts Used
- CSV file handling  
- Data validation and error handling  
- Functions and modular programming  
- User authentication logic  
- Lists, dictionaries, and loops  

### Skills Demonstrated
- Python scripting  
- File I/O (CSV)  
- Data management and persistence  
- Menu-driven program design  
- Input validation and error handling  
