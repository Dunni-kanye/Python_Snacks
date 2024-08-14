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

        elif choice == 2:
            account_number = int(input("Enter your account number: "))
            if account_number in account_numbers:
                index = account_numbers.index(account_number)
                print(f"Account number {account_number} closed successfully.")
                account_numbers.pop(index)
                balances.pop(index)
                pins.pop(index)
            else:
                print("Account not found.")

        elif choice == 3:
            account_number = int(input("Enter your account number: "))
            if account_number in account_numbers:
                index = account_numbers.index(account_number)
                amount = float(input("Enter deposit amount: "))
                if amount > 0:
                    balances[index] += amount
                    print(f"Deposit successful! New balance: ${balances[index]}")
                else:
                    print("Invalid deposit amount.")
            else:
                print("Account not found.")

        elif choice == 4:
            account_number = int(input("Enter your account number: "))
            if account_number in account_numbers:
                index = account_numbers.index(account_number)
                amount = float(input("Enter withdrawal amount: "))
                if 0 < amount <= balances[index]:
                    balances[index] -= amount
                    print(f"Withdrawal successful! New balance: ${balances[index]}")
                else:
                    print("Invalid withdrawal amount or insufficient funds.")
            else:
                print("Account not found.")

        elif choice == 5:
            account_number = int(input("Enter your account number: "))
            if account_number in account_numbers:
                index = account_numbers.index(account_number)
                print(f"Your current balance is: ${balances[index]}")
            else:
                print("Account not found.")

        elif choice == 6:
            account_number = int(input("Enter your account number: "))
            if account_number in account_numbers:
                index = account_numbers.index(account_number)
                recipient_account = int(input("Enter the recipient's account number: "))
                if recipient_account in account_numbers:
                    recipient_index = account_numbers.index(recipient_account)
                    transfer_amount = float(input("Enter transfer amount: "))

                    if 0 < transfer_amount <= balances[index]:
                        balances[index] -= transfer_amount
                        balances[recipient_index] += transfer_amount
                        print("Transfer successful!")
                        print(f"Your new balance: ${balances[index]}")
                        print(f"Recipient's new balance: ${balances[recipient_index]}")

                        generate_receipt = input("Would you like to generate a receipt? (yes/no): ")
                        if generate_receipt.lower() == "yes":
                            print("\n---------- Transfer Receipt --------------------------")
                            print(f"Sender Account: {account_number}")
                            print(f"Recipient Account: {recipient_account}")
                            print(f"Transfer Amount: ${transfer_amount}")
                            print("------------------------------------------------------------\n")
                    else:
                        print("Invalid transfer amount or insufficient funds.")
                else:
                    print("Recipient account not found.")
            else:
                print("Your account number not found.")


ATM_app()