# Reading two numbers from the keyboard
# We use float() to handle both integers and decimals
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Finding the minimum using the ternary operator
min_val = num1 if num1 < num2 else num2

print(f"The minimum value is: {min_val}")