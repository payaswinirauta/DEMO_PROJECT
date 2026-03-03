# ATM Program for Google Colab

from IPython.display import clear_output

# Initial setup
balance = 10000
correct_pin = "1234"

# Allow only 3 PIN attempts
for attempt in range(3):
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("PIN accepted. Welcome!\n")
        break
    else:
        print("Incorrect PIN!")
else:
    print("3 wrong attempts. Your account is blocked.")
    exit()

# Main menu loop
while True:
    clear_output(wait=True)  # Clear previous output for clean display
    print("--- ATM Menu ---")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
            print(f"Withdrawal successful! New balance: {balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposit successful! New balance: {balance}")

    elif choice == "3":
        print(f"Your current balance is: {balance}")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1-4.")

    input("\nPress Enter to continue...")  # Pause to let user read output