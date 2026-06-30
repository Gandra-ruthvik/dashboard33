# Program to perform arithmetic operations on two numbers

# Taking input from the user
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

# Arithmetic operations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

# Display results
print("\nResults:")
print("Addition =", addition)
print("Subtraction =", subtraction)
print("Multiplication =", multiplication)

# Division with error handling
if second_number != 0:
    division = first_number / second_number
    print("Division =", division)
else:
    print("Error: Division by zero is not allowed.")