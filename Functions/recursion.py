# Simple Recursion Code


def sum_of_integers(n):  # Recursion
    if n == 1:  # Base case
        return 1
    else:  # Recursive case
        return n + sum_of_integers(n - 1)  # Recursive call


# Example usage
result = sum_of_integers(5)
print("Sum of integers from 1 to 5:", result)  # Output: 15


def show(n):  # Recursion
    if n == 0:  # Base case
        return  # If not, the infinity loop will occur.
    print(n)  # Output: 5 4 3 2 1
    show(n - 1)  # Recursive call
    print("End")  # Output: End End End End End


show(5)  # Output: 5 4 3 2 1 End End End End End


# Factorial using Recursion
def factorial(n):  # Recursion
    if n == 0 or n == 1:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)  # Recursive call


# Example usage
result = factorial(5)
print("Factorial of 5:", result)  # Output: 120
