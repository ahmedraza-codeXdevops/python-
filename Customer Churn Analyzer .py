customers = [
    {"id": 101, "name": "Ahmed", "plan": "Premium", "months": 18, "monthly_bill": 999, "churn": "No"},
    {"id": 102, "name": "Rahul", "plan": "Basic", "months": 3, "monthly_bill": 399, "churn": "Yes"},
    {"id": 103, "name": "Priya", "plan": "Premium", "months": 24, "monthly_bill": 999, "churn": "No"},
    {"id": 104, "name": "Aman", "plan": "Standard", "months": 7, "monthly_bill": 599, "churn": "Yes"},
    {"id": 105, "name": "Sara", "plan": "Premium", "months": 30, "monthly_bill": 999, "churn": "No"},
    {"id": 106, "name": "Rohit", "plan": "Basic", "months": 2, "monthly_bill": 399, "churn": "Yes"},
    {"id": 107, "name": "Neha", "plan": "Standard", "months": 14, "monthly_bill": 599, "churn": "No"},
    {"id": 108, "name": "Arjun", "plan": "Premium", "months": 5, "monthly_bill": 999, "churn": "Yes"},
    {"id": 109, "name": "Karan", "plan": "Basic", "months": 20, "monthly_bill": 399, "churn": "No"},
    {"id": 110, "name": "Anjali", "plan": "Standard", "months": 4, "monthly_bill": 599, "churn": "Yes"}
]


def show_customers():
    print("\n--- CUSTOMER DATA ---")

    for customer in customers:
        print(
            f"ID: {customer['id']} | "
            f"Name: {customer['name']} | "
            f"Plan: {customer['plan']} | "
            f"Months: {customer['months']} | "
            f"Bill: ₹{customer['monthly_bill']} | "
            f"Churn: {customer['churn']}"
        )


def total_customers():
    print("\nTotal Customers:", len(customers))


def churn_analysis():
    churned = sum(
        1 for customer in customers
        if customer["churn"] == "Yes"
    )

    active = len(customers) - churned

    churn_rate = (churned / len(customers)) * 100

    print("\n--- CHURN ANALYSIS ---")
    print("Total Customers:", len(customers))
    print("Active Customers:", active)
    print("Churned Customers:", churned)
    print(f"Churn Rate: {churn_rate:.2f}%")


def plan_analysis():
    plans = {}

    for customer in customers:
        plan = customer["plan"]

        if plan not in plans:
            plans[plan] = {
                "total": 0,
                "churned": 0
            }

        plans[plan]["total"] += 1

        if customer["churn"] == "Yes":
            plans[plan]["churned"] += 1

    print("\n--- PLAN ANALYSIS ---")

    for plan, data in plans.items():
        rate = (data["churned"] / data["total"]) * 100

        print(
            f"{plan}: "
            f"Customers = {data['total']}, "
            f"Churned = {data['churned']}, "
            f"Churn Rate = {rate:.2f}%"
        )


def high_risk_customers():
    print("\n--- HIGH RISK CUSTOMERS ---")

    found = False

    for customer in customers:
        if customer["months"] <= 6:
            print(
                f"{customer['name']} | "
                f"Plan: {customer['plan']} | "
                f"Months: {customer['months']} | "
                f"Churn: {customer['churn']}"
            )
            found = True

    if not found:
        print("No high-risk customers found.")


def churned_customers():
    print("\n--- CHURNED CUSTOMERS ---")

    for customer in customers:
        if customer["churn"] == "Yes":
            print(
                f"{customer['name']} | "
                f"Plan: {customer['plan']} | "
                f"Monthly Bill: ₹{customer['monthly_bill']}"
            )


def revenue_analysis():
    total_revenue = sum(
        customer["monthly_bill"]
        for customer in customers
    )

    lost_revenue = sum(
        customer["monthly_bill"]
        for customer in customers
        if customer["churn"] == "Yes"
    )

    remaining_revenue = total_revenue - lost_revenue

    print("\n--- REVENUE ANALYSIS ---")
    print(f"Monthly Revenue: ₹{total_revenue:,}")
    print(f"Revenue Lost From Churn: ₹{lost_revenue:,}")
    print(f"Remaining Revenue: ₹{remaining_revenue:,}")


def longest_customers():
    print("\n--- LONGEST CUSTOMERS ---")

    sorted_customers = sorted(
        customers,
        key=lambda x: x["months"],
        reverse=True
    )

    for customer in sorted_customers[:5]:
        print(
            f"{customer['name']} - "
            f"{customer['months']} months"
        )


def search_customer():
    name = input("\nEnter customer name: ")

    found = False

    for customer in customers:
        if customer["name"].lower() == name.lower():
            print("\nCustomer Found")
            print("ID:", customer["id"])
            print("Name:", customer["name"])
            print("Plan:", customer["plan"])
            print("Months:", customer["months"])
            print("Monthly Bill:", f"₹{customer['monthly_bill']}")
            print("Churn:", customer["churn"])

            found = True
            break

    if not found:
        print("Customer not found.")


def main():

    while True:

        print("\n==============================")
        print("       CUSTOMER CHURN")
        print("          ANALYZER")
        print("==============================")

        print("1. Show Customers")
        print("2. Total Customers")
        print("3. Churn Analysis")
        print("4. Plan Analysis")
        print("5. High Risk Customers")
        print("6. Churned Customers")
        print("7. Revenue Analysis")
        print("8. Longest Customers")
        print("9. Search Customer")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_customers()

        elif choice == "2":
            total_customers()

        elif choice == "3":
            churn_analysis()

        elif choice == "4":
            plan_analysis()

        elif choice == "5":
            high_risk_customers()

        elif choice == "6":
            churned_customers()

        elif choice == "7":
            revenue_analysis()

        elif choice == "8":
            longest_customers()

        elif choice == "9":
            search_customer()

        elif choice == "10":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


main()