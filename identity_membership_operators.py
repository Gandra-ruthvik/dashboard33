"""
Identity and Membership Operators Program
Demonstrates the use of identity operators (is, is not) and membership 
operators (in, not in) to check object identity and element membership.
"""

def identity_operators_demo():
    """
    Demonstrate identity operators (is, is not).
    These check if two variables refer to the same object in memory.
    """
    print("=" * 70)
    print("IDENTITY OPERATORS (is, is not) DEMONSTRATION")
    print("=" * 70)
    
    print("\nIdentity operators check if two variables refer to the SAME OBJECT")
    print("(i.e., the same memory location), not if they have the same value.")
    
    print("\n" + "-" * 70)
    print("1. Identity with Lists")
    print("-" * 70)
    
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1
    
    print(f"\nlist1 = {list1}")
    print(f"list2 = {list2}")
    print(f"list3 = list1")
    
    print(f"\nlist1 is list2: {list1 is list2}")
    print(f"  (Same content but different objects in memory)")
    
    print(f"\nlist1 is list3: {list1 is list3}")
    print(f"  (list3 refers to the same object as list1)")
    
    print(f"\nlist1 == list2: {list1 == list2}")
    print(f"  (Same content, so equality comparison returns True)")
    
    print(f"\nlist1 is not list2: {list1 is not list2}")
    print(f"list1 is not list3: {list1 is not list3}")
    
    print("\n" + "-" * 70)
    print("2. Identity with Integers (Python Optimization)")
    print("-" * 70)
    
    a = 10
    b = 10
    c = 256
    d = 256
    e = 257
    f = 257
    
    print(f"\nSmall integers are cached by Python:")
    print(f"a = 10, b = 10")
    print(f"a is b: {a is b} (Python caches small integers for optimization)")
    
    print(f"\nLarge integers beyond 256 are not cached:")
    print(f"e = 257, f = 257")
    print(f"e is f: {e is f} (Even though they're equal: {e == f})")
    
    print("\n" + "-" * 70)
    print("3. Identity with None")
    print("-" * 70)
    
    value1 = None
    value2 = None
    value3 = ""
    
    print(f"\nNone is a special singleton object in Python:")
    print(f"value1 = None")
    print(f"value2 = None")
    print(f"value3 = ''")
    
    print(f"\nvalue1 is None: {value1 is None}")
    print(f"value1 is value2: {value1 is value2}")
    print(f"value3 is None: {value3 is None}")
    print(f"\n(Correct way to check for None: use 'is None', not '== None')")
    
    print("\n" + "-" * 70)
    print("4. Identity with Booleans")
    print("-" * 70)
    
    bool1 = True
    bool2 = True
    bool3 = 1 == 1  # This evaluates to True
    
    print(f"\nbool1 = True")
    print(f"bool2 = True")
    print(f"bool3 = 1 == 1  (evaluates to True)")
    
    print(f"\nbool1 is bool2: {bool1 is bool2}")
    print(f"bool1 is bool3: {bool1 is bool3}")
    print(f"(True and False are singleton objects in Python)")
    
    print("\n" + "=" * 70)


def membership_operators_demo():
    """
    Demonstrate membership operators (in, not in).
    These check if an element is present in a sequence.
    """
    print("\n\n" + "=" * 70)
    print("MEMBERSHIP OPERATORS (in, not in) DEMONSTRATION")
    print("=" * 70)
    
    print("\nMembership operators check if an element exists in a sequence")
    print("(lists, tuples, sets, strings, dictionaries, etc.)")
    
    print("\n" + "-" * 70)
    print("1. Membership in Lists")
    print("-" * 70)
    
    fruits = ["apple", "banana", "orange", "grape", "kiwi"]
    print(f"\nfruits = {fruits}")
    
    print(f"\n'apple' in fruits: {'apple' in fruits}")
    print(f"'mango' in fruits: {'mango' in fruits}")
    print(f"'banana' not in fruits: {'banana' not in fruits}")
    print(f"'pineapple' not in fruits: {'pineapple' not in fruits}")
    
    print("\n" + "-" * 70)
    print("2. Membership in Strings")
    print("-" * 70)
    
    text = "Hello Python"
    print(f"\ntext = '{text}'")
    
    print(f"\n'Hello' in text: {'Hello' in text}")
    print(f"'python' in text: {'python' in text} (case-sensitive)")
    print(f"'Python' in text: {'Python' in text}")
    print(f"'xyz' not in text: {'xyz' not in text}")
    print(f"' ' in text: {' ' in text} (space is present)")
    
    print("\n" + "-" * 70)
    print("3. Membership in Tuples")
    print("-" * 70)
    
    coordinates = (10, 20, 30)
    print(f"\ncoordinates = {coordinates}")
    
    print(f"\n20 in coordinates: {20 in coordinates}")
    print(f"40 in coordinates: {40 in coordinates}")
    print(f"10 not in coordinates: {10 not in coordinates}")
    print(f"100 not in coordinates: {100 not in coordinates}")
    
    print("\n" + "-" * 70)
    print("4. Membership in Sets")
    print("-" * 70)
    
    colors = {"red", "blue", "green", "yellow"}
    print(f"\ncolors = {colors}")
    
    print(f"\n'red' in colors: {'red' in colors}")
    print(f"'purple' in colors: {'purple' in colors}")
    print(f"'blue' not in colors: {'blue' not in colors}")
    print(f"'orange' not in colors: {'orange' not in colors}")
    
    print("\n" + "-" * 70)
    print("5. Membership in Dictionaries (checks keys)")
    print("-" * 70)
    
    person = {"name": "John", "age": 30, "city": "New York"}
    print(f"\nperson = {person}")
    
    print(f"\n'name' in person: {'name' in person} (checks keys)")
    print(f"'John' in person: {'John' in person} (values are not checked)")
    print(f"'age' in person: {'age' in person}")
    print(f"'email' not in person: {'email' not in person}")
    
    # Checking for values in dictionary
    print(f"\n'John' in person.values(): {'John' in person.values()}")
    print(f"30 in person.values(): {30 in person.values()}")
    
    print("\n" + "=" * 70)


def practical_membership_example():
    """
    Practical examples of using membership operators.
    """
    print("\n\n" + "=" * 70)
    print("PRACTICAL EXAMPLE: MEMBERSHIP OPERATORS IN ACTION")
    print("=" * 70)
    
    try:
        # Example 1: Checking user input
        print("\n" + "-" * 70)
        print("Example 1: Validating Input")
        print("-" * 70)
        
        valid_grades = ['A', 'B', 'C', 'D', 'F']
        grade = input("\nEnter a grade (A/B/C/D/F): ").upper()
        
        if grade in valid_grades:
            print(f"✓ '{grade}' is a valid grade")
        else:
            print(f"✗ '{grade}' is not a valid grade")
        
        # Example 2: Checking character in string
        print("\n" + "-" * 70)
        print("Example 2: Character Check in String")
        print("-" * 70)
        
        password = input("\nEnter a password: ")
        
        has_uppercase = any(c.isupper() for c in password)
        has_lowercase = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*" for c in password)
        
        print(f"\nPassword Requirements Check:")
        print(f"  Contains uppercase: {has_uppercase}")
        print(f"  Contains lowercase: {has_lowercase}")
        print(f"  Contains digit: {has_digit}")
        print(f"  Contains special char (!@#$%^&*): {has_special}")
        
        if has_uppercase and has_lowercase and has_digit:
            print(f"  ✓ Password meets basic requirements!")
        else:
            print(f"  ✗ Password needs improvement.")
        
    except Exception as e:
        print(f"Error: {e}")


def membership_with_ranges():
    """
    Membership operators with ranges and complex data structures.
    """
    print("\n\n" + "=" * 70)
    print("MEMBERSHIP OPERATORS WITH COMPLEX STRUCTURES")
    print("=" * 70)
    
    # List of tuples
    print("\n1. List of Tuples:")
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
    print(f"   students = {students}")
    print(f"   ('Alice', 85) in students: {('Alice', 85) in students}")
    print(f"   ('Alice', 90) in students: {('Alice', 90) in students}")
    
    # Nested lists
    print("\n2. Nested Lists:")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"   matrix = {matrix}")
    print(f"   [1, 2, 3] in matrix: {[1, 2, 3] in matrix}")
    print(f"   Note: Need exact match, including order and structure")
    
    # String operations
    print("\n3. Substring Search:")
    sentence = "The quick brown fox jumps over the lazy dog"
    print(f"   sentence = '{sentence}'")
    print(f"   'quick brown' in sentence: {'quick brown' in sentence}")
    print(f"   'quick' in sentence: {'quick' in sentence}")
    print(f"   'slow' not in sentence: {'slow' not in sentence}")
    
    # Dictionary keys and values
    print("\n4. Dictionary Search:")
    inventory = {"apple": 10, "banana": 5, "orange": 8}
    print(f"   inventory = {inventory}")
    print(f"   'apple' in inventory: {'apple' in inventory} (key search)")
    print(f"   10 in inventory.values(): {10 in inventory.values()} (value search)")


def combined_example():
    """
    Example combining identity and membership operators.
    """
    print("\n\n" + "=" * 70)
    print("COMBINED EXAMPLE: IDENTITY AND MEMBERSHIP TOGETHER")
    print("=" * 70)
    
    # Create lists
    original_list = [1, 2, 3, 4, 5]
    copy_list = [1, 2, 3, 4, 5]
    reference_list = original_list
    
    print(f"\noriginal_list = {original_list}")
    print(f"copy_list = {copy_list}")
    print(f"reference_list = original_list")
    
    print("\n" + "-" * 70)
    print("Identity Checks:")
    print("-" * 70)
    print(f"original_list is reference_list: {original_list is reference_list}")
    print(f"original_list is copy_list: {original_list is copy_list}")
    
    print("\n" + "-" * 70)
    print("Membership Checks:")
    print("-" * 70)
    print(f"3 in original_list: {3 in original_list}")
    print(f"3 in copy_list: {3 in copy_list}")
    print(f"10 not in original_list: {10 not in original_list}")
    
    print("\n" + "-" * 70)
    print("Combined Check Example:")
    print("-" * 70)
    
    search_value = 3
    if search_value in original_list and reference_list is original_list:
        print(f"✓ {search_value} is in original_list AND reference_list")
        print(f"  points to the same object as original_list")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    identity_operators_demo()
    membership_operators_demo()
    practical_membership_example()
    membership_with_ranges()
    combined_example()
