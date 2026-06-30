
def compare_numbers(num1, num2):
    if num1 > num2:
        print(f"{num1} is larger than {num2}.")
    elif num1 < num2:
        print(f"{num2} is larger than {num1}.")
    else:
        print("Both numbers are equal.")
def check_range(number, lower=10, upper=20):
    if number >= lower and number <= upper:
        print("The number is within the specified range.")
    else:
        print("The number is not within the specified range.")
    if string and len(string) > 5:
        print("The string is not empty and its length is greater than 5 characters.")
def simple_calculator(operation, num1, num2):
    if operation == "add":
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif operation == "subtract":
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif operation == "multiply":
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please choose add, subtract, multiply, or divide.")
def classify_age(age):
    if age < 13:
        print("You are classified as a child.")
    elif 13 <= age < 20:
        print("You are classified as a teenager.")
    elif 20 <= age < 65:
        print("You are classified as an adult.")
    else:
        print("You are classified as a senior.")
def login_system(username, password):
    valid_username = "admin"
    valid_password = "password123"
    
    if username == valid_username and password == valid_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")