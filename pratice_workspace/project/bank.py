# Simple CLI Banking System using dicts and nested data structures

accounts = {}       # Format: {acc_no: (name, balance)}
transactions = {}   # Format: {acc_no: [transaction logs]}

def create_account():
    acc_no = input("Enter new account number: ")
    if acc_no in accounts:
        print("Account already exists.")
        return
    name = input("Enter account holder name: ")
    try:
        balance = float(input("Enter initial deposit: "))
        if balance < 0:
            raise ValueError
    except ValueError:
        print("Invalid amount.")
        return
    accounts[acc_no] = (name, balance)
    transactions[acc_no] = [f"Account created with balance {balance:.2f}"]
    print(f"Account {acc_no} created successfully.")

def deposit():
    acc_no = input("Enter account no: ")
    if acc_no not in accounts:
        print("Invalid account number.")
        return
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid amount.")
        return
    name, balance = accounts[acc_no]
    balance += amount
    accounts[acc_no] = (name, balance)
    transactions[acc_no].append(f"Deposited {amount:.2f}")
    print(f"Deposited successfully. New Balance: {balance:.2f}")

def withdraw():
    acc_no = input("Enter account no: ")
    if acc_no not in accounts:
        print("Invalid account number.")
        return
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid amount.")
        return
    name, balance = accounts[acc_no]
    if amount > balance:
        print("Insufficient balance.")
        return
    balance -= amount
    accounts[acc_no] = (name, balance)
    transactions[acc_no].append(f"Withdrew {amount:.2f}")
    print(f"Withdrawn successfully. New Balance: {balance:.2f}")

def transfer():
    from_acc = input("Enter sender account no: ")
    to_acc = input("Enter receiver account no: ")
    if from_acc not in accounts or to_acc not in accounts:
        print("Invalid account number(s).")
        return
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid amount.")
        return
    from_name, from_bal = accounts[from_acc]
    to_name, to_bal = accounts[to_acc]
    if amount > from_bal:
        print("Insufficient balance.")
        return
    from_bal -= amount
    to_bal += amount
    accounts[from_acc] = (from_name, from_bal)
    accounts[to_acc] = (to_name, to_bal)
    transactions[from_acc].append(f"Transferred {amount:.2f} to {to_acc}")
    transactions[to_acc].append(f"Received {amount:.2f} from {from_acc}")
    print(f"Transferred {amount:.2f} from {from_acc} to {to_acc}")

def view_transactions():
    acc_no = input("Enter account no: ")
    if acc_no not in transactions:
        print("Invalid account number.")
        return
    print(f"Transactions for {acc_no}:")
    for t in transactions[acc_no]:
        print(" -", t)

def main():
    while True:
        print("\nWelcome to CLI Bank")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Transactions")
        print("6. Exit")
        choice = input("Choose option: ")
        
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
            print("Exiting. Thank you for using CLI Bank.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

