# Finance Tracker

A command-line personal finance tracker built in Python. Log income and expenses, view your transaction history, and track your balance — all saved locally between sessions.

## Features

- Add income and expense transactions with descriptions
- View all transactions in a numbered list
- Check current balance, total income, and total expenses
- Delete individual transactions
- Auto-saves data to a local JSON file on exit

## How to Run

Make sure you have Python 3 installed, then run:
```bash
python Finance_Tracker.py
```

## Usage

When you launch the app you'll see a menu:
```
1. Add Transaction
2. View All Transactions
3. View Balance
4. Delete a Transaction
5. Exit
```

Select an option by entering the corresponding number. Your data is saved automatically when you choose option 5 to exit.

## Data Storage

Transactions are saved to `data.json` in the same directory. This file is created automatically on first use and loaded on every subsequent run.

## Tech Stack

- Python 3
- JSON (standard library)
