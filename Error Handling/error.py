# Exception Handling for Division

# try block is used to catch exceptions
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)

# except block is used to handle the exception
except ZeroDivisionError:
    print("Cannot divide by zero.")

# except block is used to handle the exception if previous blocks do not match the condition.
except ValueError:
    print("Invalid input.")


# Determining Voting Age
def check_voting_age(age):
    try:
        if age < 18:
            raise ValueError("Age is below voting age")
        else:
            print("You are eligible to vote!")
    except ValueError as e:
        print(e)


# Test cases
check_voting_age(20)  # Eligible
check_voting_age(16)  # Below voting age
