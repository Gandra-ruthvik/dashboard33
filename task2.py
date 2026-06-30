# Complete requirement 'Create a Python program that asks the user for their age and then uses conditional statements to determine and print whether the user is eligible to vote (assuming the voting age is 18 years old).' as defined in the assignment.
# Complete requirement 'Write a Python function that takes a grade (as a percentage) as input and uses conditional statements to return the corresponding letter grade (A for 90-100%, B for 80-89%, C for 70-79%, D for 60-69%, and F for below 60%).' as defined in the assignment.
# Complete requirement 'Develop a simple calculator program in Python that uses conditional statements to perform different mathematical operations (addition, subtraction, multiplication, division) based on the user's choice.' as defined in the assignment.
# Complete requirement 'Implement a Python program that generates a random number between 1 and 100 and uses conditional statements to guess whether the number is odd or even, providing feedback to the user.' as defined in the assignment
def check_voting_eligibility(age):
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
def get_letter_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
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
def guess_odd_even(number):
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
        