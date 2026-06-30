"""
Comparison Operators Program
Demonstrates the use of comparison operators (>, <, ==, !=, >=, <=)
to compare two numbers and determine relationships.
"""

def compare_numbers():
    """
    Compare two numbers using comparison operators.
    Takes two numbers as input and displays comparison results.
    """
    print("=" * 70)
    print("NUMBER COMPARISON USING COMPARISON OPERATORS")
    print("=" * 70)
    
    try:
        # Get input from user
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("\n" + "-" * 70)
        print("COMPARISON RESULTS")
        print("-" * 70)
        
        # Greater than (>)
        result_greater = num1 > num2
        print(f"\n1. Greater than (>)")
        print(f"   Is {num1} > {num2}? {result_greater}")
        if result_greater:
            print(f"   ✓ {num1} is greater than {num2}")
        
        # Less than (<)
        result_less = num1 < num2
        print(f"\n2. Less than (<)")
        print(f"   Is {num1} < {num2}? {result_less}")
        if result_less:
            print(f"   ✓ {num1} is less than {num2}")
        
        # Equal to (==)
        result_equal = num1 == num2
        print(f"\n3. Equal to (==)")
        print(f"   Is {num1} == {num2}? {result_equal}")
        if result_equal:
            print(f"   ✓ {num1} is equal to {num2}")
        
        # Not equal to (!=)
        result_not_equal = num1 != num2
        print(f"\n4. Not equal to (!=)")
        print(f"   Is {num1} != {num2}? {result_not_equal}")
        if result_not_equal:
            print(f"   ✓ {num1} is not equal to {num2}")
        
        # Greater than or equal to (>=)
        result_greater_equal = num1 >= num2
        print(f"\n5. Greater than or equal to (>=)")
        print(f"   Is {num1} >= {num2}? {result_greater_equal}")
        if result_greater_equal:
            print(f"   ✓ {num1} is greater than or equal to {num2}")
        
        # Less than or equal to (<=)
        result_less_equal = num1 <= num2
        print(f"\n6. Less than or equal to (<=)")
        print(f"   Is {num1} <= {num2}? {result_less_equal}")
        if result_less_equal:
            print(f"   ✓ {num1} is less than or equal to {num2}")
        
        # Summary
        print("\n" + "-" * 70)
        print("SUMMARY")
        print("-" * 70)
        
        if num1 > num2:
            print(f"→ {num1} is LARGER than {num2}")
        elif num1 < num2:
            print(f"→ {num1} is SMALLER than {num2}")
        else:
            print(f"→ {num1} and {num2} are EQUAL")
        
        print("=" * 70)
        
    except ValueError:
        print("Error: Please enter valid numerical values!")


def compare_numbers_with_function(num1, num2):
    """
    Function to compare two numbers using comparison operators.
    Returns a string describing the relationship.
    """
    print(f"\nComparing {num1} and {num2}:")
    
    if num1 > num2:
        print(f"  {num1} > {num2} → {num1} is larger")
        return f"{num1} is larger"
    elif num1 < num2:
        print(f"  {num1} < {num2} → {num1} is smaller")
        return f"{num1} is smaller"
    elif num1 == num2:
        print(f"  {num1} == {num2} → They are equal")
        return "Numbers are equal"
    elif num1 >= num2:
        print(f"  {num1} >= {num2} → {num1} is greater or equal")
        return f"{num1} is greater or equal"
    elif num1 <= num2:
        print(f"  {num1} <= {num2} → {num1} is less or equal")
        return f"{num1} is less or equal"


def comparison_examples():
    """Demonstrate various comparison operations with examples"""
    print("\n\n" + "=" * 70)
    print("PREDEFINED COMPARISON EXAMPLES")
    print("=" * 70)
    
    test_cases = [
        (10, 5),
        (3, 8),
        (7, 7),
        (-5, 2),
        (0, 0),
        (3.5, 3.5),
    ]
    
    for num1, num2 in test_cases:
        compare_numbers_with_function(num1, num2)
        print()


def comparison_with_variables():
    """Demonstrate comparison operators with various data types"""
    print("\n" + "=" * 70)
    print("COMPARISON OPERATORS WITH VARIABLES")
    print("=" * 70)
    
    a = 15
    b = 25
    c = 15
    
    print(f"\nGiven variables: a = {a}, b = {b}, c = {c}")
    print(f"\nComparison results:")
    print(f"  a > b:  {a} > {b} = {a > b}")
    print(f"  a < b:  {a} < {b} = {a < b}")
    print(f"  a == c: {a} == {c} = {a == c}")
    print(f"  a != b: {a} != {b} = {a != b}")
    print(f"  a >= c: {a} >= {c} = {a >= c}")
    print(f"  b <= c: {b} <= {c} = {b <= c}")


if __name__ == "__main__":
    compare_numbers()
    comparison_examples()
    comparison_with_variables()
