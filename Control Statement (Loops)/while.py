# Simple while loop

count = 1  # Initialize count to 1
while count <= 5:  # Loop will run until count is less than or equal to 5
    print("Hello, world!")
    count = +1  # Increment count by 1


# Print multiplication table of a number n
n = 5
print(f"Multiplication table of {n}:")
i = 1
while i <= 10:  # Loop will run until i is less than or equal to 10
    print(f"{n} x {i} = {n*i}")  # the f before a string literal denotes an f-string.
    i += 1  # Increment i by 1


# Find the first even number in a list
# break statement
numbers = [1, 3, 5, 7, 8, 9, 10, 12]
found = False
i = 0
while i < len(numbers):  # Loop will run until i is less than the length of the list
    if numbers[i] % 2 == 0:
        print("First even number found:", numbers[i])
        found = True
        break  # Exit the loop after finding the first even number
    i += 1

if not found:
    print("No even number found in the list.")


# Print odd numbers from 1 to 10, skipping even numbers
# continue statement
i = 1
while i <= 10:  # Loop will run until i is less than or equal to 10
    if i % 2 == 0:
        i += 1
        continue  # Skip the even number
    print(i)
    i += 1
