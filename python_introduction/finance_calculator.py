# A python script that calculates that calculates user's monthly savings based on their inputed monthly income and expenses.It will then project these savings
# over a year, assuming a fixed interest rate thus demonstarting compound interest's effect on savings.
#User Input for Financial Details:

#Prompt the user for their monthly income: “Enter your monthly income: ”.
#Ask for their total monthly expenses: “Enter your total monthly expenses: ”.
monthly_income = int(input("Enter your monthly income:  "))
monthly_expenses = int(input("Enter your total monthly expenses:  "))

# Calculate Monthly Savings:

# Calculate the monthly savings by subtracting monthly expenses from the monthly income.
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings:

annual_savings = monthly_savings * 12
projected_savings = annual_savings + int(annual_savings * 0.05)

# Output Results:

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest,  is: ${projected_savings}.")