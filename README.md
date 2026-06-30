# Python Operators - Comprehensive Guide

This project contains a comprehensive collection of Python programs demonstrating all major types of operators in Python. Each program includes interactive examples, practical use cases, and detailed explanations.

## 📁 Project Structure

```
special operators/
├── main.py                              # Main menu program (start here!)
├── arithmetic_operators.py              # Arithmetic operators demo
├── comparison_operators.py              # Comparison operators demo
├── logical_operators.py                 # Logical operators demo
├── assignment_operators.py              # Assignment operators demo
├── identity_membership_operators.py     # Identity & Membership operators demo
└── README.md                            # This file
```

## 🚀 Getting Started

### Running the Main Program
To start the interactive menu, run:
```bash
python main.py
```

This will launch a menu interface where you can select which operator type you want to explore.

### Running Individual Programs
You can also run individual programs directly:

```bash
python arithmetic_operators.py
python comparison_operators.py
python logical_operators.py
python assignment_operators.py
python identity_membership_operators.py
```

## 📚 Program Details

### 1. Arithmetic Operators (`arithmetic_operators.py`)
**Operators:** `+`, `-`, `*`, `/`, `%`, `**`

**Topics Covered:**
- Addition (+) - Adding length and width for perimeter calculation
- Subtraction (-) - Calculating differences
- Multiplication (*) - Calculating area of rectangle
- Division (/) - Dividing dimensions
- Modulus (%) - Finding remainders
- Exponentiation (**) - Power calculations

**Features:**
- Interactive rectangle area and perimeter calculator
- Input validation
- Practical demonstrations of all arithmetic operators
- Real-world examples (dimensions, calculations)

**Example Usage:**
```python
length = 10
width = 5
area = length * width          # Multiplication
perimeter = 2 * (length + width)  # Combination of operators
```

---

### 2. Comparison Operators (`comparison_operators.py`)
**Operators:** `>`, `<`, `==`, `!=`, `>=`, `<=`

**Topics Covered:**
- Greater than (>) - Comparing if one number is larger
- Less than (<) - Comparing if one number is smaller
- Equal to (==) - Checking equality
- Not equal to (!=) - Checking inequality
- Greater than or equal to (>=) - Combined comparison
- Less than or equal to (<=) - Combined comparison

**Features:**
- Interactive number comparison tool
- Predefined comparison examples
- Relationship determination (larger, smaller, equal)
- Practical applications

**Example Usage:**
```python
num1 = 10
num2 = 20
if num1 > num2:
    print("num1 is larger")
elif num1 < num2:
    print("num1 is smaller")
else:
    print("They are equal")
```

---

### 3. Logical Operators (`logical_operators.py`)
**Operators:** `and`, `or`, `not`

**Topics Covered:**
- AND operator - Both conditions must be True
- OR operator - At least one condition must be True
- NOT operator - Reverses the boolean value
- Range checking (combining with comparison operators)
- String pattern matching
- Complex conditional statements

**Features:**
- Interactive range checker (check if number is in range)
- String pattern matching (vowels, length, patterns)
- Practical examples (age verification, holiday determination)
- Loop and complex logic demonstrations

**Example Usage:**
```python
age = 25
has_license = True

# AND - both conditions must be true
can_drive = age >= 18 and has_license

# OR - at least one must be true
is_holiday = False
is_weekend = True
can_rest = is_holiday or is_weekend

# NOT - reverses boolean
is_raining = False
can_go_out = not is_raining
```

---

### 4. Assignment Operators (`assignment_operators.py`)
**Operators:** `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`

**Topics Covered:**
- Simple assignment (=)
- Addition assignment (+=)
- Subtraction assignment (-=)
- Multiplication assignment (*=)
- Division assignment (/=)
- Modulus assignment (%=)
- Exponentiation assignment (**=)
- Comparison of regular vs augmented assignment

**Features:**
- Interactive calculator using augmented assignment
- Loop examples with augmented operators
- String concatenation with +=
- Demonstration of differences and best practices
- Multiple practical examples

**Example Usage:**
```python
# Regular assignment
x = 5
x = x + 10  # x is now 15

# Augmented assignment (same result, more concise)
y = 5
y += 10  # y is now 15

# Augmented assignment in loops
total = 0
for i in range(1, 6):
    total += i  # Adds each number to total
```

---

### 5. Identity and Membership Operators (`identity_membership_operators.py`)
**Operators:** `is`, `is not`, `in`, `not in`

**Topics Covered:**

#### Identity Operators:
- `is` - Checks if two variables refer to the same object
- `is not` - Checks if two variables are different objects
- Memory location comparison
- Python optimization (integer caching, None, True/False)

#### Membership Operators:
- `in` - Checks if element exists in a sequence
- `not in` - Checks if element doesn't exist
- Works with lists, tuples, strings, sets, dictionaries
- Substring searching

**Features:**
- Interactive membership checking
- Password validation example
- Nested data structure handling
- Dictionary key/value searching
- Combined identity and membership examples

**Example Usage:**
```python
# Identity operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 is list2)   # False (different objects)
print(list1 is list3)   # True (same object)
print(list1 == list2)   # True (same content)

# Membership operators
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)        # True
print("grape" not in fruits)    # True
print("n" in "banana")          # True (substring)
```

---

## 📊 Operator Precedence

When multiple operators are used, Python evaluates them in this order (highest to lowest):

1. `**` (Exponentiation)
2. `+x`, `-x`, `~x` (Unary operators)
3. `*`, `/`, `//`, `%` (Multiplication, Division, Modulus)
4. `+`, `-` (Addition, Subtraction)
5. `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` (Comparisons)
6. `not` (Logical NOT)
7. `and` (Logical AND)
8. `or` (Logical OR)

Use parentheses to override precedence: `(2 + 3) * 4` → 20 (not 14)

---

## 💡 Key Learning Points

### Arithmetic Operators
- Used for mathematical calculations
- `/` returns float, `//` returns integer
- `%` is useful for checking even/odd, cycling through values
- `**` can be used for powers and square roots

### Comparison Operators
- Always return Boolean (True/False)
- Can be chained: `1 < x < 10`
- `==` checks value equality, `is` checks object identity

### Logical Operators
- `and` has higher precedence than `or`
- Short-circuit evaluation: `or` stops if first is True, `and` stops if first is False
- `not` has highest precedence among logical operators

### Assignment Operators
- Augmented assignment is more readable and concise
- `+=` is frequently used for accumulation
- Works with strings: `message += "more text"`

### Identity Operators
- `is` checks memory location, `==` checks value
- Always use `is None`, never `== None`
- Small integers (-5 to 256) are cached in Python

### Membership Operators
- `in` works with all sequences and collections
- For dictionaries, `in` checks keys by default
- Use `.values()` to check dictionary values

---

## 🎯 Practice Exercises

1. **Arithmetic**: Modify the rectangle calculator to also calculate the diagonal length
2. **Comparison**: Create a program that grades test scores
3. **Logical**: Build a password strength validator
4. **Assignment**: Write a program that accumulates statistics
5. **Identity/Membership**: Create a contact list with duplicate detection

---

## 🔍 Common Mistakes to Avoid

1. **Using `=` in comparison**: Use `==` to compare, not `=`
   ```python
   if x == 5:  # Correct
   if x = 5:   # Wrong (syntax error)
   ```

2. **Confusing `and`/`or` precedence**:
   ```python
   # Correct grouping with parentheses
   if (x > 5) and (y < 10) or (z == 0):
   ```

3. **Using `is` for value comparison**:
   ```python
   x = [1, 2, 3]
   y = [1, 2, 3]
   print(x is y)   # False (different objects)
   print(x == y)   # True (same content)
   ```

4. **Forgetting None is special**:
   ```python
   if value is None:      # Correct
   if value == None:      # Works but not recommended
   ```

---

## 📝 Examples of Combined Operators

```python
# Using multiple operator types together
result = 10 + 5 * 2          # Arithmetic: 20 (precedence matters)
result = 5 > 3 and 10 < 20   # Comparison + Logical: True

# Finding common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = [x for x in list1 if x in list2]  # Membership: [3, 4]

# Complex conditions
if (age >= 18 and age <= 65) and (income > 0 or benefits) and status is not None:
    print("Eligible")
```

---

## 🎓 Resources for Further Learning

- Python Official Documentation: https://docs.python.org/3/
- PEP 8 (Python Style Guide): https://www.python.org/dev/peps/pep-0008/
- Real Python Operator Guides: https://realpython.com/

---

## 📄 License

This educational project is free to use and modify for learning purposes.

---

## ✨ Summary

This comprehensive guide covers all major Python operators with:
- ✅ 5 separate, focused programs
- ✅ Interactive examples and user input
- ✅ Real-world practical applications
- ✅ Detailed explanations and comments
- ✅ Common mistakes and best practices
- ✅ Menu-driven interface for easy navigation

Happy learning! 🐍
