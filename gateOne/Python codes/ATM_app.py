import random

def ATM_app():
    account_numbers = []
    balances = []
    pins = []

    print("Welcome")
    print("Kindly type Next to select an option:")
    next_option = input()

    transactions = True

    while transactions:
        print("\n--- ATM Machine ---")
        print("1. Create an account")
        print("2. Close account")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Check Account balance")
        print("6. Transfer from one account to another")
        print("7. Change Pin")
        print("8. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            print("Create account")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            pin = input("Enter a 4-digit PIN: ")

            if len(pin) != 4:
                print("Invalid PIN. Account creation failed.")
                continue

            account_number = random.randint(100000, 999999)
            account_numbers.append(account_number)
            balances.append(0.0)
            pins.append(pin)
            print("Account successfully created")
            print(f"Your account number is: {account_number}")









ATM_app()




	