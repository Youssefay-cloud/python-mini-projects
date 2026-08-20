
def show_balance(balance):
    print("-------------------------------")
    return f"your balance is {balance}" 
    print("-------------------------------")

def deposit():
    print("-------------------------------")
    amount = int(input("please enter an amount to be desposited: "))
    print("-------------------------------")
    if amount < 0 :
        print("This is not a valid amount")
        return 0 
    else :
        return amount

def withdraw(balance):
    print("-------------------------------")
    amount = int(input("please enter an amount to be withdrawn: "))
    print("-------------------------------")
    if amount < 0 :
        print("This is not a valid amount")
        return 0
    elif amount > balance:
        print("Not enough money to withdraw")
        return 0 
    else :
        return amount




def main(): 
    balance = 0 
    is_running = True

    while is_running :

        print("Welcom to your account")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("-------------------------------")

        choice = input("please choose from (1, 2, 3, 4)")

        if choice == '1':
            print(show_balance(balance))
            print("-------------------------------")
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance = balance-withdraw(balance)
        elif choice == '4':
            is_running = False
        else :
            print("Choose from the displayed numbers")


if __name__ == "__main__":
    main()