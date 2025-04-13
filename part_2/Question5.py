
'''5.Write a program to find the simple interest when the value of principle, rate of interest and time period is provided by the user.['''
def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest"""
    interest = (principal * rate * time) / 100
    return interest

# Get input from user
print("Simple Interest Calculator")
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in % per annum): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = calculate_simple_interest(principal, rate, time)
total_amount = principal + simple_interest

# Display results
print(f"\nSimple Interest Calculation Results:")
print(f"Principal Amount: ₹{principal:.2f}")
print(f"Rate of Interest: {rate}% per annum")
print(f"Time Period: {time} years")
print(f"Simple Interest: ₹{simple_interest:.2f}")
print(f"Total Amount: ₹{total_amount:.2f}")