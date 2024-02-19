# Simple for loop

num = [1, 2, 3, 4, 5]
for n in num:  # Loop through each number in the list
    print(n)


# Print multiplication table of a number n
n = int(input("Enter a number: "))  # Get the number from the user
print("Multiplication table of ", n)
for i in range(1, 11):  # Loop will run 10 times
    print(f"{n} x {i} = {n*i}")
# the f before a string literal denotes an f-string, also known as a formatted string literal as range is from 1 to 10


# Find the first even number in a list
# break statement
numbers = [1, 3, 5, 7, 8, 9, 10]
for num in numbers:  # Loop through each number in the list
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break  # Exit the loop after finding the first even number
else:
    print("No even number found in the list.")


# Print all numbers in a list except for the ones divisible by 3
# continue statement
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:  # Loop through each number in the list
    if num % 3 == 0:
        continue  # Skip the number if it is divisible by 3
    print(num)


# Simple for loop with range

for i in range(5):  # Loop will run 5 times
    print("Hello, world!")


# Finding the first prime number in a range
# break statement
start = 10
end = 20
for num in range(start, end + 1):  # Loop through each number in the range
    if num > 1:  # Check if the number is greater than 1
        for i in range(2, num):  # Loop through each number from 2 to num - 1
            if (num % i) == 0:  # Check if the number is divisible by i
                break  # Exit the loop if the number is not prime
        else:
            print(
                f"The first prime number in the range {start} to {end} is:", num
            )  # the f before a string literal denotes an f-string, also known as a formatted string literal
            print(
                "The first prime number in the range", start, "to", end, "is:", num
            )  # simple format
            break  # Exit the loop after finding the first prime number


# Print multiples of 3 from 1 to 20
# continue statement
for i in range(1, 21):
    if i % 3 != 0:  # Skip the number if it is not divisible by 3
        continue  # Skip the number if it is not divisible by 3
    print(i)
