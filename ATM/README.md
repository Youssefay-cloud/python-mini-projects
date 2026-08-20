# ATM Console Application

This project is a simple command-line ATM simulator written in Python. It allows a user to check their balance, deposit money, withdraw money, and exit the program.

## Project Purpose

The app demonstrates basic Python programming concepts such as:
- Variables and functions
- Input/output handling
- Conditionals
- Loops
- Simple validation for financial transactions

## Features

The program includes the following menu options:

1. Show Balance
2. Deposit
3. Withdraw
4. Exit

### 1. Show Balance
Displays the current balance in the account.

### 2. Deposit
Prompts the user to enter an amount to deposit. The value must be a positive number.
- If the entered amount is negative, the app prints a validation message and does not change the balance.

### 3. Withdraw
Prompts the user to enter an amount to withdraw.
- If the amount is negative, the app rejects it.
- If the withdrawal amount is greater than the current balance, the app prints an error and does not change the balance.

### 4. Exit
Stops the program loop and ends the application.

## How the App Works

The main logic is contained in the `main()` function.

- The variable `balance` starts at `0`.
- A `while` loop keeps the ATM menu open until the user selects exit.
- Each menu choice calls a related function:
  - `show_balance(balance)`
  - `deposit()`
  - `withdraw(balance)`

## Functions in the Code

### `show_balance(balance)`
Returns a formatted message showing the current account balance.

### `deposit()`
Reads the deposit amount from the user and validates it.

### `withdraw(balance)`
Reads the withdrawal amount, validates it, and ensures the user has enough funds.

### `main()`
Creates the interactive ATM menu and processes the chosen option.

## Virtual Environment Setup

This project includes a virtual environment named `venv`. Activate it before running the app.

### On Linux or macOS

```bash
cd /workspaces/python-mini-projects
source venv/bin/activate
cd ATM
python app.py
```

### On Windows

```bash
cd C:\path\to\python-mini-projects
venv\Scripts\activate
cd ATM
python app.py
```

## Running the App

After activating the virtual environment, run:

```bash
cd /workspaces/python-mini-projects/ATM
python app.py
```

## Example Interaction

```text
Welcom to your account
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
please choose from (1, 2, 3, 4)
```

If the user selects:
- `1`: shows the current balance
- `2`: asks for an amount to deposit
- `3`: asks for an amount to withdraw
- `4`: exits the program

## Notes

This is a beginner-friendly project designed to practice Python fundamentals. It uses a simple in-memory balance, so the balance resets every time the program starts.
