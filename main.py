"""
Main Program: Python Operators Comprehensive Guide
This program provides a menu interface to access all operator demonstrations.
"""

import os
import sys

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_main_menu():
    """Display the main menu."""
    clear_screen()
    print("\n" + "=" * 70)
    print("PYTHON OPERATORS - COMPREHENSIVE GUIDE")
    print("=" * 70)
    print("\nSelect an option to explore different types of operators:\n")
    print("1. Arithmetic Operators (+, -, *, /, %, **)")
    print("   Calculate area and perimeter of a rectangle")
    print()
    print("2. Comparison Operators (>, <, ==, !=, >=, <=)")
    print("   Compare two numbers and determine relationships")
    print()
    print("3. Logical Operators (and, or, not)")
    print("   Evaluate conditional statements and patterns")
    print()
    print("4. Assignment Operators (=, +=, -=, *=, /=, %=, **=)")
    print("   Update variable values with different assignment methods")
    print()
    print("5. Identity and Membership Operators (is, is not, in, not in)")
    print("   Check object identity and element membership")
    print()
    print("6. View Information about all operators")
    print()
    print("7. Exit")
    print("\n" + "=" * 70)


def show_operator_info():
    """Display comprehensive information about all operators."""
    clear_screen()
    print("\n" + "=" * 70)
    print("PYTHON OPERATORS - INFORMATION GUIDE")
    print("=" * 70)
    
    operators_info = {
        "ARITHMETIC OPERATORS": {
            "description": "Used to perform mathematical operations",
            "operators": {
                "+": "Addition",
                "-": "Subtraction",
                "*": "Multiplication",
                "/": "Division (returns float)",
                "//": "Floor Division (returns integer)",
                "%": "Modulus (remainder after division)",
                "**": "Exponentiation (power)"
            }
        },
        "COMPARISON OPERATORS": {
            "description": "Used to compare values; return True or False",
            "operators": {
                "==": "Equal to",
                "!=": "Not equal to",
                ">": "Greater than",
                "<": "Less than",
                ">=": "Greater than or equal to",
                "<=": "Less than or equal to"
            }
        },
        "LOGICAL OPERATORS": {
            "description": "Used to combine conditional statements",
            "operators": {
                "and": "Returns True if both conditions are True",
                "or": "Returns True if at least one condition is True",
                "not": "Reverses the result (returns opposite boolean)"
            }
        },
        "ASSIGNMENT OPERATORS": {
            "description": "Used to assign values to variables",
            "operators": {
                "=": "Simple assignment",
                "+=": "Add and assign (equivalent to x = x + y)",
                "-=": "Subtract and assign (equivalent to x = x - y)",
                "*=": "Multiply and assign (equivalent to x = x * y)",
                "/=": "Divide and assign (equivalent to x = x / y)",
                "%=": "Modulus and assign (equivalent to x = x % y)",
                "**=": "Exponentiation and assign (equivalent to x = x ** y)"
            }
        },
        "IDENTITY OPERATORS": {
            "description": "Used to compare if two objects are identical (same memory location)",
            "operators": {
                "is": "Returns True if both variables are the same object",
                "is not": "Returns True if both variables are not the same object"
            }
        },
        "MEMBERSHIP OPERATORS": {
            "description": "Used to test if a value exists in a sequence",
            "operators": {
                "in": "Returns True if element is in a sequence",
                "not in": "Returns True if element is not in a sequence"
            }
        }
    }
    
    for operator_type, info in operators_info.items():
        print(f"\n{operator_type}")
        print("-" * 70)
        print(f"Description: {info['description']}")
        print("\nOperators:")
        for op, description in info['operators'].items():
            print(f"  {op:10} → {description}")
    
    print("\n" + "=" * 70)
    print("\nKey Points:")
    print("• Operators are symbols that perform specific operations on operands")
    print("• Different operators have different precedence (order of evaluation)")
    print("• Parentheses can be used to override default precedence")
    print("• Understanding operators is fundamental to programming")
    print("=" * 70)
    
    input("\nPress Enter to return to main menu...")


def run_arithmetic_operators():
    """Run the arithmetic operators program."""
    clear_screen()
    try:
        from arithmetic_operators import calculate_rectangle_properties, arithmetic_examples
        calculate_rectangle_properties()
        arithmetic_examples()
    except ImportError:
        print("Error: Could not import arithmetic_operators module")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress Enter to return to main menu...")


def run_comparison_operators():
    """Run the comparison operators program."""
    clear_screen()
    try:
        from comparison_operators import compare_numbers, comparison_examples, comparison_with_variables
        compare_numbers()
        comparison_examples()
        comparison_with_variables()
    except ImportError:
        print("Error: Could not import comparison_operators module")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress Enter to return to main menu...")


def run_logical_operators():
    """Run the logical operators program."""
    clear_screen()
    try:
        from logical_operators import check_number_range, string_pattern_matching, logical_operator_examples
        check_number_range()
        string_pattern_matching()
        logical_operator_examples()
    except ImportError:
        print("Error: Could not import logical_operators module")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress Enter to return to main menu...")


def run_assignment_operators():
    """Run the assignment operators program."""
    clear_screen()
    try:
        from assignment_operators import (
            assignment_operator_demo,
            augmented_assignment_operators,
            practical_example_calculator,
            loop_example_with_augmented_assignment,
            comparison_assignment_vs_augmented
        )
        assignment_operator_demo()
        augmented_assignment_operators()
        practical_example_calculator()
        loop_example_with_augmented_assignment()
        comparison_assignment_vs_augmented()
    except ImportError:
        print("Error: Could not import assignment_operators module")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress Enter to return to main menu...")


def run_identity_membership_operators():
    """Run the identity and membership operators program."""
    clear_screen()
    try:
        from identity_membership_operators import (
            identity_operators_demo,
            membership_operators_demo,
            practical_membership_example,
            membership_with_ranges,
            combined_example
        )
        identity_operators_demo()
        membership_operators_demo()
        practical_membership_example()
        membership_with_ranges()
        combined_example()
    except ImportError:
        print("Error: Could not import identity_membership_operators module")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress Enter to return to main menu...")


def main():
    """Main program loop."""
    while True:
        display_main_menu()
        
        try:
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                run_arithmetic_operators()
            elif choice == '2':
                run_comparison_operators()
            elif choice == '3':
                run_logical_operators()
            elif choice == '4':
                run_assignment_operators()
            elif choice == '5':
                run_identity_membership_operators()
            elif choice == '6':
                show_operator_info()
            elif choice == '7':
                clear_screen()
                print("\n" + "=" * 70)
                print("Thank you for using Python Operators Guide!")
                print("=" * 70 + "\n")
                sys.exit(0)
            else:
                print("\nInvalid choice! Please enter a number between 1 and 7.")
                input("Press Enter to continue...")
        
        except KeyboardInterrupt:
            clear_screen()
            print("\n" + "=" * 70)
            print("Program interrupted by user.")
            print("=" * 70 + "\n")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
