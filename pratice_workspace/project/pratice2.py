accounts = {}  # {"1001": ("mia", 500), "1002": ("john", 200)}
transactions = {}  # {"1001": ["created account with 500", "deposited 500"]}

def main():
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Transactions")
        print("6. Exit")
        choice = input("Choose an option from 1 to 6: ")
        
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            view_transactions()
        elif choice == "6":
            print("Exiting. Thank you for using CLI bank.")
            break
        else:
            print("Invalid choice")

def create_account():
    account_num = input("Enter new user account number: ")
    if account_num in accounts:
        print("Account already exists")
        return
    name = input("Enter user name: ")
    try:
        balance = float(input("Enter initial deposit amount: "))
        if balance < 0:
            raise ValueError
    except ValueError:
        print("Invalid amount")
        return
    accounts[account_num] = (name, balance)
    transactions[account_num] = [f"Created account with balance {balance}"]
    print(f"Account {account_num} created successfully")

def deposit():
    account_num = input("Enter account number: ")
    if account_num not in accounts:
        print("Invalid account number")
        return
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid amount")
        return
    name, balance = accounts[account_num]
    balance += amount
    accounts[account_num] = (name, balance)
    transactions[account_num].append(f"Deposited {amount}")
    print(f"Deposited successfully. New balance: {balance}")

def withdraw():
    account_num = input("Enter account number: ")
    if account_num not in accounts:
        print("Invalid account number")
        return
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid amount")
        return
    name, balance = accounts[account_num]
    if amount > balance:
        print("Insufficient balance")
        return
    balance -= amount
    accounts[account_num] = (name, balance)
    transactions[account_num].append(f"Withdrew {amount}")
    print(f"Withdrawn successfully. New balance: {balance}")

def transfer():
    sender_acc = input("Enter sender account number: ")
    receiver_acc = input("Enter receiver's account number: ")
    if sender_acc not in accounts or receiver_acc not in accounts:
        print("Invalid account number")
        return
    try:
        amount = float(input("Enter transfer amount: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid amount")
        return
    sender_name, sender_bal = accounts[sender_acc]
    receiver_name, receiver_bal = accounts[receiver_acc]
    if amount > sender_bal:
        print("Insufficient balance")
        return
    sender_bal -= amount
    receiver_bal += amount
    accounts[sender_acc] = (sender_name, sender_bal)
    accounts[receiver_acc] = (receiver_name, receiver_bal)
    transactions[sender_acc].append(f"Transferred {amount} to {receiver_acc}")
    transactions[receiver_acc].append(f"Received {amount} from {sender_acc}")
    print(f"Transferred {amount} from {sender_acc} to {receiver_acc}")

def view_transactions():
    account_num = input("Enter account number: ")
    if account_num not in transactions:
        print("Invalid account number")
        return
    print(f"Transactions for {account_num}:")
    for t in transactions[account_num]:
        print("-", t)

if __name__ == "__main__":
    main()
