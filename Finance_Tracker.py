# This app is going to track finances it will do a few things.
# - The first is it will add expenses, second is that it will be able to show all expenses.
# - Show total spending.
# - Create a menu loop.

# - Be able to save it 

import json

transactions = []

output_file = 'data.json'


balance = 0
income_balance = 0
expense_balance = 0

try:
    with open(output_file, 'r') as json_file:
        transactions = json.load(json_file)
    for t in transactions:
        if t['type'] == 'income':
            balance += t['amount']
            income_balance += t['amount']
        elif t['type'] == 'expense':
            balance -= t['amount']
            expense_balance += t['amount']
except FileNotFoundError:
    transactions = []


while True: 
    
    print("Please enter a number 1 - 5")
    
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. View Balance")
    print("4. Delete a Transaction")
    print("5. Exit")
    
    menu = int(input("\n"))
    
    if menu == 1:
        amount = float(input("\n Amount: "))
        income_expense = input("Income or expense: ")
        transaction_description = input("Name: ")
        income_expense = income_expense.lower().strip()
        
        if income_expense not in ["income", "expense"]:
            print("Not a type")
            continue
        
        if income_expense == "income":
            balance += amount
            income_balance += amount
        elif income_expense == "expense":
            balance -= amount
            expense_balance += amount
            
        transac = {
            
            "amount": amount,
            "type": income_expense,
            "transaction_description": transaction_description
            
        }
        
        transactions.append(transac)
        
    elif menu == 2:
        for i, items in enumerate(transactions, start=1):
            print(f"{i}. Name: {items['transaction_description']} Amount: {items['amount']} | Type: {items['type']}")

    elif menu == 3:
        print(f"Current balance: {balance}")
        print(f"Total income: {income_balance}")
        print(f"Total expenses: {expense_balance}")
        
    elif menu == 4:
        delete_transaction = int(input("\nWhich number transaction would you like to delete: "))
    
        if 1 <= delete_transaction <= len(transactions):
            removed = transactions[delete_transaction-1]
            
            if removed ['type'] == "income":
                balance -= removed['amount']
                income_balance -= removed['amount']
            elif removed['type'] == "expense":
                balance += removed['amount']
                expense_balance -= removed['amount']
            
            del transactions[delete_transaction-1]
            print(f"Transaction {delete_transaction} was deleted! ")
        else:
            print("not in the list! ")        
    elif menu == 5:
        
        with open(output_file, 'w') as json_file:
            json.dump(transactions, json_file, indent=4)
        
        break
    
    else:
        print("Not a menu option! ")
    
    


