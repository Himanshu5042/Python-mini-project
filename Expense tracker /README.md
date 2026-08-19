# 💰 Expense Tracker

A simple **Python Expense Tracker** that helps users record, view, calculate, and search their daily expenses.

This project is designed as a beginner-friendly Python mini-project to practice **functions, lists, dictionaries, loops, conditional statements, and exception handling**.

## 📌 Features

* Add new expenses
* Store date, category, amount, and description
* View all recorded expenses
* Calculate total spending
* Search expenses by category
* Handle invalid amount input
* Simple command-line interface

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements
* Exception Handling

## 📂 Project Structure

```text
expense-tracker/
│
├── expense_tracker.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/expense-tracker.git
```

### 2. Open the project folder

```bash
cd expense-tracker
```

### 3. Run the Python program

```bash
python expense_tracker.py
```

## 💻 Example

```text
==============================
       EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Total Expenses
4. Search by Category
5. Exit

Enter your choice: 1

--- Add Expense ---
Enter date (DD-MM-YYYY): 19-08-2026
Enter category: Food
Enter amount: 250
Enter description: Lunch

Expense added successfully!
```

### Viewing Expenses

```text
--- All Expenses ---

Expense 1
Date: 19-08-2026
Category: Food
Amount: ₹ 250.0
Description: Lunch

Expense 2
Date: 19-08-2026
Category: Transport
Amount: ₹ 80.0
Description: Bus ticket
```

### Total Expenses

```text
--- Total Expenses ---
Total Spending: ₹330.00
```

## 🔍 How the Project Works

The program stores each expense as a Python dictionary:

```python
expense = {
    "date": date,
    "category": category,
    "amount": amount,
    "description": description
}
```

All expense dictionaries are stored inside a list:

```python
expenses = []
```

The program provides a menu where the user can choose different operations.

### 1. Add Expense

The user enters:

* Date
* Category
* Amount
* Description

The information is stored in the `expenses` list.

### 2. View Expenses

The program displays all expenses stored in the list.

### 3. Calculate Total

The `sum()` function calculates the total amount spent.

```python
total = sum(expense["amount"] for expense in expenses)
```

### 4. Search by Category

The program compares the entered category with the category stored in each expense and displays matching records.

## 📚 Python Concepts Practiced

This project helps you understand:

* Variables
* User input
* Lists
* Dictionaries
* Functions
* `for` loops
* `while` loops
* `if-elif-else`
* String methods
* `sum()`
* Exception handling
* Formatted output

## 🔮 Future Improvements

The project can be improved by adding:

* [ ] Save expenses permanently using CSV
* [ ] SQLite database support
* [ ] Monthly expense reports
* [ ] Expense editing and deletion
* [ ] Budget limit feature
* [ ] Expense charts using Matplotlib
* [ ] GUI using Tkinter
* [ ] Export expenses to Excel
* [ ] Login system
* [ ] Automatic monthly summaries

## 🎯 Project Objective

The main objective of this project is to create a simple application for managing personal expenses while gaining practical experience with Python programming concepts.

## 👨‍💻 Author

**Himanshu Verma**

Python Mini Project — Expense Tracker
