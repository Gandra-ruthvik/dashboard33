"""
Assignment Operators Program
Demonstrates the use of assignment (=) and augmented assignment operators 
(+=, -=, *=, /=, %=, **=) to update variable values.
"""

def assignment_operator_demo():
    """
    Demonstrate the basic assignment operator (=).
    """
    print("=" * 70)
    print("ASSIGNMENT OPERATOR (=) DEMONSTRATION")
    print("=" * 70)
    
    print("\nThe assignment operator (=) assigns a value to a variable.")
    print("\nExamples:")
    
    # Simple assignment
    x = 10
    print(f"\n1. Simple Assignment:")
    print(f"   x = 10")
    print(f"   x = {x}")
    
    # Assignment with expression
    y = x + 5
    print(f"\n2. Assignment with Expression:")
    print(f"   y = x + 5 = {x} + 5")
    print(f"   y = {y}")
    
    # Multiple assignment
    a, b, c = 1, 2, 3
    print(f"\n3. Multiple Assignment:")
    print(f"   a, b, c = 1, 2, 3")
    print(f"   a = {a}, b = {b}, c = {c}")
    
    # Swapping values
    p, q = 100, 200
    print(f"\n4. Swapping Values (before):")
    print(f"   p = {p}, q = {q}")
    p, q = q, p
    print(f"   After swap using: p, q = q, p")
    print(f"   p = {p}, q = {q}")


def augmented_assignment_operators():
    """
    Demonstrate all augmented assignment operators with examples.
    """
    print("\n\n" + "=" * 70)
    print("AUGMENTED ASSIGNMENT OPERATORS DEMONSTRATION")
    print("=" * 70)
    
    # Addition Assignment (+=)
    print("\n" + "-" * 70)
    print("1. Addition Assignment (+=)")
    print("-" * 70)
    num = 15
    print(f"   Initial: num = {num}")
    print(f"   Operation: num += 5")
    num += 5
    print(f"   After: num = {num}")
    print(f"   Explanation: num += 5 is equivalent to num = num + 5")
    
    # Subtraction Assignment (-=)
    print("\n" + "-" * 70)
    print("2. Subtraction Assignment (-=)")
    print("-" * 70)
    num = 20
    print(f"   Initial: num = {num}")
    print(f"   Operation: num -= 3")
    num -= 3
    print(f"   After: num = {num}")
    print(f"   Explanation: num -= 3 is equivalent to num = num - 3")
    
    # Multiplication Assignment (*=)
    print("\n" + "-" * 70)
    print("3. Multiplication Assignment (*=)")
    print("-" * 70)
    num = 8
    print(f"   Initial: num = {num}")
    print(f"   Operation: num *= 4")
    num *= 4
    print(f"   After: num = {num}")
    print(f"   Explanation: num *= 4 is equivalent to num = num * 4")
    
    # Division Assignment (/=)
    print("\n" + "-" * 70)
    print("4. Division Assignment (/=)")
    print("-" * 70)
    num = 50
    print(f"   Initial: num = {num}")
    print(f"   Operation: num /= 2")
    num /= 2
    print(f"   After: num = {num}")
    print(f"   Explanation: num /= 2 is equivalent to num = num / 2")
    
    # Modulus Assignment (%=)
    print("\n" + "-" * 70)
    print("5. Modulus Assignment (%=)")
    print("-" * 70)
    num = 17
    print(f"   Initial: num = {num}")
    print(f"   Operation: num %= 5")
    num %= 5
    print(f"   After: num = {num}")
    print(f"   Explanation: num %= 5 is equivalent to num = num % 5")
    
    # Exponentiation Assignment (**=)
    print("\n" + "-" * 70)
    print("6. Exponentiation Assignment (**=)")
    print("-" * 70)
    num = 2
    print(f"   Initial: num = {num}")
    print(f"   Operation: num **= 5")
    num **= 5
    print(f"   After: num = {num}")
    print(f"   Explanation: num **= 5 is equivalent to num = num ** 5")
    
    print("\n" + "=" * 70)


def practical_example_calculator():
    """
    Practical example using augmented assignment operators:
    A simple calculator that accumulates values.
    """
    print("\n\n" + "=" * 70)
    print("PRACTICAL EXAMPLE: CALCULATOR USING AUGMENTED ASSIGNMENT")
    print("=" * 70)
    
    try:
        result = 0
        print(f"\nStarting with result = {result}")
        
        print("\nPerforming calculations:")
        
        # Addition
        print(f"\n1. Add 10: result += 10")
        result += 10
        print(f"   result = {result}")
        
        # Multiplication
        print(f"\n2. Multiply by 2: result *= 2")
        result *= 2
        print(f"   result = {result}")
        
        # Subtraction
        print(f"\n3. Subtract 5: result -= 5")
        result -= 5
        print(f"   result = {result}")
        
        # Division
        print(f"\n4. Divide by 3: result /= 3")
        result /= 3
        print(f"   result = {result:.2f}")
        
        # Modulus
        print(f"\n5. Modulus 4: result %= 4")
        result_int = int(result)
        result = result_int % 4
        print(f"   result = {result}")
        
        # Exponentiation
        print(f"\n6. Power 2: result **= 2")
        result **= 2
        print(f"   result = {result}")
        
        print(f"\nFinal result: {result}")
        
    except ValueError:
        print("Error: Invalid input!")


def loop_example_with_augmented_assignment():
    """
    Example of using augmented assignment operators in loops.
    """
    print("\n\n" + "=" * 70)
    print("LOOP EXAMPLE: AUGMENTED ASSIGNMENT IN ITERATIONS")
    print("=" * 70)
    
    # Sum of numbers using +=
    print("\n1. Sum of numbers 1 to 5 using +=")
    total = 0
    print(f"   Initial total = {total}")
    for i in range(1, 6):
        total += i
        print(f"   total += {i} → total = {total}")
    print(f"   Final sum: {total}")
    
    # Product of numbers using *=
    print("\n2. Product of numbers 1 to 5 using *=")
    product = 1
    print(f"   Initial product = {product}")
    for i in range(1, 6):
        product *= i
        print(f"   product *= {i} → product = {product}")
    print(f"   Final product: {product}")
    
    # String concatenation using +=
    print("\n3. String concatenation using +=")
    message = ""
    print(f"   Initial message = '{message}'")
    words = ["Hello", " ", "Python", " ", "Operators"]
    for word in words:
        message += word
        print(f"   message += '{word}' → message = '{message}'")
    print(f"   Final message: '{message}'")


def comparison_assignment_vs_augmented():
    """
    Compare regular assignment with augmented assignment.
    """
    print("\n\n" + "=" * 70)
    print("COMPARISON: REGULAR vs AUGMENTED ASSIGNMENT")
    print("=" * 70)
    
    print("\n" + "-" * 70)
    print("Example: Adding 10 to a variable")
    print("-" * 70)
    
    # Regular assignment
    x = 5
    print(f"\nRegular Assignment:")
    print(f"  x = 5")
    print(f"  x = x + 10")
    x = x + 10
    print(f"  x = {x}")
    
    # Augmented assignment
    y = 5
    print(f"\nAugmented Assignment:")
    print(f"  y = 5")
    print(f"  y += 10")
    y += 10
    print(f"  y = {y}")
    
    print(f"\nBoth produce the same result: x = {x}, y = {y}")
    print(f"But augmented assignment is more concise and readable!")
    
    print("\nAdvantages of Augmented Assignment:")
    print("  • More readable and concise")
    print("  • Less error-prone (no typos in variable names)")
    print("  • Slightly more efficient in some cases")
    print("  • Standard in many programming languages")


if __name__ == "__main__":
    assignment_operator_demo()
    augmented_assignment_operators()
    practical_example_calculator()
    loop_example_with_augmented_assignment()
    comparison_assignment_vs_augmented()
