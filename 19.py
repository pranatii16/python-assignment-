def track_expenses():
    expenses = {}
    
    print("Enter your daily expenses for the week:\n")
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        while True:
            try:
                amount = float(input(f"{day}: ₹"))
                expenses[day] = amount
                break
            except ValueError:
                print("Please enter a valid number.")

    with open("weekly_expenses.txt", "w", encoding="utf-8") as file:
        for day, amount in expenses.items():
            file.write(f"{day}: ₹{amount}\n")

    
    total = sum(expenses.values())
    average = total / 7
    max_day = max(expenses, key=expenses.get)
    min_day = min(expenses, key=expenses.get)

    print("\n Weekly Summary:")
    print(f"Total Expenses: ₹{total:.2f}")
    print(f"Average Daily Expense: ₹{average:.2f}")
    print(f"Highest Spending: {max_day} (₹{expenses[max_day]})")
    print(f"Lowest Spending: {min_day} (₹{expenses[min_day]})")

track_expenses()

