# `if-elif-else` statement is used to check multiple conditions.
light = input("Enter the color of the light: ")

# `if` statement is used to check a condition.
if light == "red":
    print("Stop")

# `elif` statement is used to check another condition if the first condition is false.
elif light == "yellow":
    print("Slow down")

elif light == "green":
    print("Go")
    
# `else` statement is used to check the condition if all the above conditions are false.
else:
    print("Light is not working properly.")


# Ternary Operator (Single Line)
food = input("Enter the name of the food: ")
eat = "Yes" if food == "Pizza" else "No" # If food is Pizza, then Yes, else No
print(eat)

# Ternary Operator (CleverIf Line)
sal = float(input("Enter the salary: "))
tax = sal * (0.1, 0.2)[sal > 50000] # 10% if salary is less than 50000, else 20%
print(tax)