transactions = [
    {"id": 1, "type": "Deposit", "category": "Salary", "amount": 30000},
    {"id": 2, "type": "Withdraw", "category": "Food", "amount": 2500},
    {"id": 3, "type": "Withdraw", "category": "Shopping", "amount": 5000},
    {"id": 4, "type": "Deposit", "category": "Freelance", "amount": 8000},
    {"id": 5, "type": "Withdraw", "category": "Travel", "amount": 3000},
]


def show_transactions():
    print("\n--- TRANSACTION HISTORY ---")

    if not transactions:
        print("No transactions found.")
        return

    for transaction in transactions:
        print(
            f"ID: {transaction['id']} | "
            f"Type: {transaction['type']} | "
            f"Category: {transaction['category']} | "
            f"Amount: ₹{transaction['amount']:,.2f}"
        )


def add_transaction():
    print("\n--- ADD TRANSACTION ---")

    transaction_type = input(
        "Enter type (Deposit/Withdraw): "
    ).capitalize()

    if transaction_type not in ["Deposit", "Withdraw"]:
        print("Invalid transaction type.")
        return

    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Enter a valid amount.")
        return

    new_id = max(
        [t["id"] for t in transactions],
        default=0
    ) + 1

    transactions.append({
        "id": new_id,
        "type": transaction_type,
        "category": category,
        "amount": amount
    })

    print("Transaction added successfully!")


def total_deposits():
    total = sum(
        t["amount"]
        for t in transactions
        if t["type"] == "Deposit"
    )

    print(f"\nTotal Deposits: ₹{total:,.2f}")


def total_withdrawals():
    total = sum(
        t["amount"]
        for t in transactions
        if t["type"] == "Withdraw"
    )

    print(f"\nTotal Withdrawals: ₹{total:,.2f}")


def current_balance():
    deposits = sum(
        t["amount"]
        for t in transactions
        if t["type"] == "Deposit"
    )

    withdrawals = sum(
        t["amount"]
        for t in transactions
        if t["type"] == "Withdraw"
    )

    balance = deposits - withdrawals

    print(f"\nCurrent Balance: ₹{balance:,.2f}")


def category_analysis():
    categories = {}

    for transaction in transactions:

        if transaction["type"] != "Withdraw":
            continue

        category = transaction["category"]

        if category not in categories:
            categories[category] = 0

        categories[category] += transaction["amount"]

    print("\n--- EXPENSE BY CATEGORY ---")

    if not categories:
        print("No expenses found.")
        return

    for category, amount in categories.items():
        print(
            f"{category}: ₹{amount:,.2f}"
        )


def highest_transaction():
    if not transactions:
        print("No transactions found.")
        return

    transaction = max(
        transactions,
        key=lambda x: x["amount"]
    )

    print("\n--- HIGHEST TRANSACTION ---")
    print("ID:", transaction["id"])
    print("Type:", transaction["type"])
    print("Category:", transaction["category"])
    print(
        "Amount:",
        f"₹{transaction['amount']:,.2f}"
    )


def search_category():
    category = input(
        "\nEnter category to search: "
    )

    found = False

    for transaction in transactions:

        if transaction["category"].lower() == category.lower():

            print(
                f"ID: {transaction['id']} | "
                f"Type: {transaction['type']} | "
                f"Amount: ₹{transaction['amount']:,.2f}"
            )

            found = True

    if not found:
        print("No transactions found.")


def transaction_summary():
    deposits = sum(
        t["amount"]
        for t in transactions
        if t["type"] == "Deposit"
    )

    withdrawals = sum(
        t["amount"]
        for t in transactions
        if t["type"] == "Withdraw"
    )

    balance = deposits - withdrawals

    print("\n==============================")
    print("     TRANSACTION SUMMARY")
    print("==============================")
    print(f"Total Deposits    : ₹{deposits:,.2f}")
    print(f"Total Withdrawals : ₹{withdrawals:,.2f}")
    print(f"Current Balance   : ₹{balance:,.2f}")
    print(
        f"Transactions      : {len(transactions)}"
    )


def main():

    while True:

        print("\n==============================")
        print("    BANK TRANSACTION")
        print("        ANALYZER")
        print("==============================")

        print("1. Show Transactions")
        print("2. Add Transaction")
        print("3. Total Deposits")
        print("4. Total Withdrawals")
        print("5. Current Balance")
        print("6. Category Analysis")
        print("7. Highest Transaction")
        print("8. Search Category")
        print("9. Transaction Summary")
        print("10. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            show_transactions()

        elif choice == "2":
            add_transaction()

        elif choice == "3":
            total_deposits()

        elif choice == "4":
            total_withdrawals()

        elif choice == "5":
            current_balance()

        elif choice == "6":
            category_analysis()

        elif choice == "7":
            highest_transaction()

        elif choice == "8":
            search_category()

        elif choice == "9":
            transaction_summary()

        elif choice == "10":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


main()