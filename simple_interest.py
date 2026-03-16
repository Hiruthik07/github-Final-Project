"""Simple Interest Calculator"""

# Input values
principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of interest: "))
time = float(input("Enter the Time (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Display result
print("Simple Interest =", simple_interest)
