accounts={} # {"1001":("mia",500),"1002":("john",200)}
transactions={} # {"1001":["created account with 500","deposited 500"]}

def main():
   while True:
      print("1. Create Account")
      print("2. Deposit")
      print("3. Withdraw")
      print("4. Transfer")
      print("5. View Transactions")
      print("6. Exit")
      choice=input("chioce an option from 1 to 6:  ")
      if choice=="1":
       create_account()
      elif choice=="2":
       deposit()
      elif choice=="3":
       withdraw()
      elif choice=="4":
       transfer()
      elif choice=="5":
       view_transactions()
      elif choice=="6":
       exit()
       print("Exiting. Thankyou for using CLI bank.")
       break
      else:
       print("invalid choice")

def create_account():
    account_num=input("Enter new user account number: ")
    if account_num in accounts():
       print("Account already exist")
       return
    name=input("Enter user name: ")
    try:
       balance=float(input("Enter initial deposit amount: "))
       if balance<0:
         raise ValueError
    except ValueError:
       print("invalid amount")
       return
    accounts[account_num]=(name,balance)
    transactions[account_num]=[f"created account with balance {balance}"]
    print(f"Account {account_num} created sucessfully")
def deposit():
    account_num=input("Enter accountnumber: ")
    if account_num not in accounts:
        print("invalid account number")
        return
    try: 
        amount= float(input("Enter deposit amount: "))
        if amount<=0:
         raise ValueError
    except ValueError:
        print("invalid amount")
        return
    name,balance=accounts[account_num]
    balance+= amount
    amount[account_num]=(name, balance)
    transactions[account_num].append (f"deposited {amount}")
    print(f" deposited successfully. New balance:{balance}")
def withdraw():
    account_num=input("Enter accountnumber: ")
    if account_num not in accounts:
        print("invalid account number")
        return
    try: 
       amount= float(input("Enter withdrew amount: "))
       if amount<=0:
        raise ValueError
    except ValueError:
        print("invalid amount")
        return
    name,balance=accounts[account_num]
    if amount>balance:
       print("insufficient balance")
       balance-= amount
       amount[account_num]=(name, balance)
       transactions[account_num].append (f"withdrew{amount}")
       print(f" withdrawn successfully. New balance:{balance}") 
def transfer():
    sender_acc=input("Enter sender account number: ")
    receiver_acc=input("Enter receivers account number: ") 
    if sender_acc not in accounts or receiver_acc not in accounts:
       print("invalid account number")
       return
    try:
       amount=float(input("Enter transfer amount: "))
       if amount<=0:
          raise ValueError
    except ValueError:
        print("invalid amount")
        return
    sender_name,sender_bal=accounts[sender_acc]
    receiver_name,receiver_bal=accounts[receiver_acc]
    if amount> sender_bal:
       print("insufficient balance")
       return
    sender_bal-=accounts
    receiver_bal+=accounts
    accounts[sender_acc]=(sender_name,sender_bal)
    accounts[receiver_acc]=(receiver_name,receiver_bal)
    transactions[sender_acc].append (f"transferred {amount} to {receiver_acc}")
    transactions[receiver_acc].append (f" received {amount} from {sender_acc}")
    print(f" transfered {amount} from {sender_acc} to {receiver_acc}")
def view_transactions():
   account_num=input("Enter account number: ")
   if account_num not in transactions():
      print("ivalid account number")
      return
   print(f"Transactions for {account_num}: ")
   for t in transactions[account_num]:
      print("-", t)
if __name__ == "__main__":
    main()
   

          











