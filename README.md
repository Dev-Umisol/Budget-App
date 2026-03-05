# 📁 Budget App
A terminal-based budget tracker built with Python classes — a freeCodeCamp certification project.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/freeCodeCamp-Certification%20Project-informational?logo=freecodecamp)

## 📌 About

This is my second freeCodeCamp certification project, built to practice object-oriented programming in Python. The app models budget categories (like Food and Clothing), supports deposits, withdrawals, and transfers between categories, and generates a visual bar chart showing spending percentages — all printed to the terminal like a receipt.

## 🧠 What I Learned

- Classes & OOP — Designing a `Category` class with its own state (`ledger`) and methods that interact with each other, such as `transfer()` calling both `withdraw()` and `deposit()` internally
- Working with lists of dictionaries — Using a ledger (a list of `{"amount": ..., "description": ...}` dicts) to model a real-world transaction history
- String formatting — Producing neatly aligned receipt-style output using f-strings with padding (e.g. `:<23` and `:>7.2f`) and the `str.center()` method
- The `math` module — Using `math.floor()` to round spending percentages down to the nearest 10 for the bar chart
- Lambda functions — Using `max()` with a `lambda` to find the longest category name dynamically for the vertical axis labels
- Guard clauses — Using a `CheckFunds()` helper to validate before any withdrawal or transfer, keeping the logic clean and reusable

## 🛠️ Technologies Used
| Tool / Library | Purpose 
|----------------|---------
|Python 3.x      | Core Language
| `math`         | Rounding percentages down with `math.floor()`

## 💡 How It Works

Each `Category` object holds a ledger — a running list of transactions. You can:
- `deposit(amount, description)` — Add funds
- `withdraw(amount, description)` — Remove funds (only if balance allows)
- `transfer(amount, category)` — Move funds between two categories
- `GetBalance()` — Return the current balance
- `print(category)` — Display a formatted receipt via __str__
The standalone `CreateSpendChart(categories)` function takes a list of categories and prints a vertical bar chart showing what percentage of total spending came from each one.

## Example Output:
```***************Food***************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96```
