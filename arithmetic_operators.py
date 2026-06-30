"""
Arithmetic Operators Program
Demonstrates the use of arithmetic operators (+, -, *, /, %, **) 
to calculate the area and perimeter of a rectangle.
"""

def calculate_rectangle_properties():
    """
    Calculate the area and perimeter of a rectangle using arithmetic operators.
    Takes length and width as input from the user.
    """
    print("=" * 60)
    print("RECTANGLE AREA AND PERIMETER CALCULATOR")
    print("=" * 60)
    
    try:
        # Get input from user
        length = float(input("\nEnter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        
        # Validate input
        if length <= 0 or width <= 0:
            print("Error: Length and width must be positive numbers!")
            return
        
        # Arithmetic operators in action
        print("\n--- Calculations ---")
        
        # Addition (+) - for perimeter
        perimeter = 2 * (length + width)
        print(f"\nPerimeter = 2 × (length + width)")
        print(f"Perimeter = 2 × ({length} + {width})")
        print(f"Perimeter = 2 × {length + width}")
        print(f"Perimeter = {perimeter} units")
        
        # Multiplication (*) - for area
        area = length * width
        print(f"\nArea = length × width")
        print(f"Area = {length} × {width}")
        print(f"Area = {area} square units")
        
        # Division (/) - average of dimensions
        average_dimension = (length + width) / 2
        print(f"\nAverage dimension = (length + width) / 2")
        print(f"Average dimension = ({length} + {width}) / 2")
        print(f"Average dimension = {length + width} / 2")
        print(f"Average dimension = {average_dimension} units")
        
        # Modulus (%) - checking if perimeter is even
        perimeter_remainder = perimeter % 2
        print(f"\nPerimeter % 2 (to check if perimeter is even): {perimeter_remainder}")
        if perimeter_remainder == 0:
            print("The perimeter is even.")
        else:
            print("The perimeter is odd.")
        
        # Exponentiation (**) - calculating area in different units
        area_in_square_cm = area * (100 ** 2)  # if dimensions are in meters
        print(f"\nArea² (exponentiation) = {area} ** 2 = {area ** 2} square units²")
        print(f"(This demonstrates the ** operator for squaring)")
        
        # Summary
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(f"Length: {length} units")
        print(f"Width: {width} units")
        print(f"Area: {area} square units")
        print(f"Perimeter: {perimeter} units")
        print(f"Average Dimension: {average_dimension} units")
        print("=" * 60)
        
    except ValueError:
        print("Error: Please enter valid numerical values!")


# Additional examples of arithmetic operators
def arithmetic_examples():
    """Demonstrate various arithmetic operations"""
    print("\n\n" + "=" * 60)
    print("ADDITIONAL ARITHMETIC OPERATOR EXAMPLES")
    print("=" * 60)
    
    num1 = 17
    num2 = 5
    
    print(f"\nGiven: num1 = {num1}, num2 = {num2}")
    print(f"Addition (+): {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction (-): {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication (*): {num1} * {num2} = {num1 * num2}")
    print(f"Division (/): {num1} / {num2} = {num1 / num2}")
    print(f"Floor Division (//): {num1} // {num2} = {num1 // num2}")
    print(f"Modulus (%): {num1} % {num2} = {num1 % num2}")
    print(f"Exponentiation (**): {num1} ** {num2} = {num1 ** num2}")


if __name__ == "__main__":
    calculate_rectangle_properties()
    arithmetic_examples()
