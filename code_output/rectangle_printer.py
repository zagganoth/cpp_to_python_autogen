# rectangle_printer.py

"""
This program prints a rectangular box with a top and bottom border of dashes,
and left and right borders of vertical bars. The middle section has 8 lines.
"""

def print_border(dash_count):
    """
    Prints a border of dashes.

    Args:
        dash_count (int): The number of dashes to print.
    """
    for _ in range(dash_count):
        print("-", end="")
    print()  # Print a newline character

def print_middle_section():
    """
    Prints the middle section of the rectangle.
    """
    for _ in range(8):  # Print 8 lines in the middle section
        print("|" + " " * 20 + "|")  # Print left border, 20 spaces, and right border

def main():
    """
    The main function that prints the rectangle.
    """
    print_border(23)  # Print top border
    print_middle_section()
    print_border(23)  # Print bottom border

if __name__ == "__main__":
    main()