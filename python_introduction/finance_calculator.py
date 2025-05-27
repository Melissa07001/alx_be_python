# finance_calculator.py

# Get user input and convert to float (to handle decimals)
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected savings after 1 year with 5% interest
projected_savings = monthly_savings * 12 * (1 + 0.05)

# Print the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
