"""
Logical Operators Program
Demonstrates the use of logical operators (and, or, not)
to evaluate conditional statements with range checking and pattern matching.
"""

def check_number_range():
    """
    Check if a number is within a certain range using logical operators (and, or).
    """
    print("=" * 70)
    print("NUMBER RANGE CHECKER USING LOGICAL OPERATORS")
    print("=" * 70)
    
    try:
        number = float(input("\nEnter a number to check: "))
        
        print("\n" + "-" * 70)
        print("RANGE CHECKING WITH LOGICAL OPERATORS")
        print("-" * 70)
        
        # Check if number is in range [0, 100] using AND operator
        in_range_0_100 = number >= 0 and number <= 100
        print(f"\n1. Is {number} between 0 and 100 (using AND)?")
        print(f"   {number} >= 0 AND {number} <= 100 = {in_range_0_100}")
        
        # Check if number is in range [10, 20] using AND operator
        in_range_10_20 = number >= 10 and number <= 20
        print(f"\n2. Is {number} between 10 and 20 (using AND)?")
        print(f"   {number} >= 10 AND {number} <= 20 = {in_range_10_20}")
        
        # Check if number is outside range [5, 15] using NOT and AND
        outside_5_15 = not (number >= 5 and number <= 15)
        print(f"\n3. Is {number} outside range [5, 15] (using NOT and AND)?")
        print(f"   NOT ({number} >= 5 AND {number} <= 15) = {outside_5_15}")
        
        # Check if number is negative or greater than 100 using OR
        negative_or_large = number < 0 or number > 100
        print(f"\n4. Is {number} negative OR greater than 100 (using OR)?")
        print(f"   {number} < 0 OR {number} > 100 = {negative_or_large}")
        
        # Multiple conditions using AND and OR
        is_single_digit = number >= 0 and number <= 9
        is_double_digit = number >= 10 and number <= 99
        is_digit_number = is_single_digit or is_double_digit
        print(f"\n5. Is {number} a single or double digit number (using OR)?")
        print(f"   (Single digit: {is_single_digit}) OR (Double digit: {is_double_digit})")
        print(f"   Result: {is_digit_number}")
        
        # Summary
        print("\n" + "-" * 70)
        print("SUMMARY")
        print("-" * 70)
        if not negative_or_large:
            print(f"✓ {number} is within the normal range [0, 100]")
        else:
            print(f"✗ {number} is outside the normal range [0, 100]")
        
        if in_range_10_20:
            print(f"✓ {number} is in the range [10, 20]")
        else:
            print(f"✗ {number} is NOT in the range [10, 20]")
        
        print("=" * 70)
        
    except ValueError:
        print("Error: Please enter a valid number!")


def string_pattern_matching():
    """
    Check if a string matches specific patterns using logical operators.
    """
    print("\n\n" + "=" * 70)
    print("STRING PATTERN MATCHING USING LOGICAL OPERATORS")
    print("=" * 70)
    
    text = input("\nEnter a string to check: ").strip().lower()
    
    print("\n" + "-" * 70)
    print("PATTERN CHECKING")
    print("-" * 70)
    
    # Check if string contains vowels using OR
    contains_vowel = 'a' in text or 'e' in text or 'i' in text or 'o' in text or 'u' in text
    print(f"\n1. Does '{text}' contain any vowel (a, e, i, o, u)?")
    print(f"   'a' in text OR 'e' in text OR ... = {contains_vowel}")
    
    # Check if string is empty or contains only spaces
    is_empty = not text or text.isspace()
    print(f"\n2. Is '{text}' empty or contains only spaces?")
    print(f"   NOT (text) OR text.isspace() = {is_empty}")
    
    # Check if string starts with 'p' and contains 'a'
    pattern1 = text.startswith('p') and 'a' in text
    print(f"\n3. Does '{text}' start with 'p' AND contain 'a'?")
    print(f"   text.startswith('p') AND 'a' in text = {pattern1}")
    
    # Check if string is all uppercase or all lowercase
    is_all_upper_or_lower = text.isupper() or text.islower()
    print(f"\n4. Is '{text}' all uppercase OR all lowercase?")
    print(f"   text.isupper() OR text.islower() = {is_all_upper_or_lower}")
    
    # Check if string length is between 3 and 10
    length_in_range = len(text) >= 3 and len(text) <= 10
    print(f"\n5. Is the length of '{text}' between 3 and 10?")
    print(f"   len(text) >= 3 AND len(text) <= 10 = {length_in_range}")
    
    # Check if string contains digits or special characters
    has_digit_or_special = any(c.isdigit() for c in text) or any(not c.isalpha() and not c.isspace() for c in text)
    print(f"\n6. Does '{text}' contain digits or special characters?")
    print(f"   Result: {has_digit_or_special}")
    
    print("=" * 70)


def logical_operator_examples():
    """Demonstrate logical operators with predefined examples"""
    print("\n\n" + "=" * 70)
    print("LOGICAL OPERATOR EXAMPLES")
    print("=" * 70)
    
    # Example 1: AND operator
    print("\n1. AND Operator Examples:")
    age = 25
    has_license = True
    can_drive = age >= 18 and has_license
    print(f"   age = {age}, has_license = {has_license}")
    print(f"   age >= 18 AND has_license = {can_drive}")
    print(f"   Can drive? {can_drive}")
    
    # Example 2: OR operator
    print("\n2. OR Operator Examples:")
    is_weekend = False
    is_holiday = True
    can_rest = is_weekend or is_holiday
    print(f"   is_weekend = {is_weekend}, is_holiday = {is_holiday}")
    print(f"   is_weekend OR is_holiday = {can_rest}")
    print(f"   Can rest? {can_rest}")
    
    # Example 3: NOT operator
    print("\n3. NOT Operator Examples:")
    is_raining = True
    can_go_out = not is_raining
    print(f"   is_raining = {is_raining}")
    print(f"   NOT is_raining = {can_go_out}")
    print(f"   Can go out? {can_go_out}")
    
    # Example 4: Complex logical expression
    print("\n4. Complex Logical Expression:")
    score = 85
    attendance = 90
    eligible_for_exam = (score >= 40 or attendance >= 75) and attendance >= 50
    print(f"   score = {score}, attendance = {attendance}")
    print(f"   (score >= 40 OR attendance >= 75) AND attendance >= 50")
    print(f"   = {eligible_for_exam}")
    print(f"   Eligible for exam? {eligible_for_exam}")
    
    # Example 5: Multiple NOT operators
    print("\n5. Multiple NOT Operators:")
    is_adult = True
    is_employed = False
    status = not (is_adult and is_employed)
    print(f"   is_adult = {is_adult}, is_employed = {is_employed}")
    print(f"   NOT (is_adult AND is_employed) = {status}")


if __name__ == "__main__":
    check_number_range()
    string_pattern_matching()
    logical_operator_examples()
