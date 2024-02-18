# Arithmetic operators
x = 10
y = 5
print("Arithmetic Operators:")
print("Addition:", x + y)  # 15
print("Subtraction:", x - y)  # 5
print("Multiplication:", x * y)  # 50
print("Division:", x / y)  # 2.0
print("Floor Division:", x // y)  # 2
print("Modulus:", x % y)  # 0
print("Exponentiation:", x**y)  # 100000
print()

# Comparison operators / Relational operators
a = 10
b = 20
print("Comparison Operators:")
print("Equal to:", a == b)  # False
print("Not Equal to:", a != b)  # True
print("Greater than:", a > b)  # False
print("Less than:", a < b)  # True
print("Greater than or equal to:", a >= b)  # False
print("Less than or equal to:", a <= b)  # True

# Assignment operators
c = 5
print("Assignment Operators:")
c += 2  # c = c + 2
print("Addition Assignment:", c)
c -= 2  # c = c - 2
print("Subtraction Assignment:", c)
c *= 2  # c = c * 2
print("Multiplication Assignment:", c)
c /= 2  # c = c / 2
print("Division Assignment:", c)
print()

# Logical operators
p = True
q = False
print("Logical Operators:")
print("AND:", p and q)  # False
print("OR:", p or q)  # True
print("NOT:", not p)  # False
print()

# Bitwise operators
m = 10
n = 5
print("Bitwise Operators:")
print("AND:", m & n)
print("OR:", m | n) 
print("XOR:", m ^ n)
print("NOT:", ~m)
print("Left Shift:", m << 1)
print("Right Shift:", m >> 1)
print()

# Membership operators
lst = [1, 2, 3, 4, 5]
print("Membership Operators:")
print("in:", 3 in lst) # True
print("not in:", 6 not in lst) # True
print()

# Identity operators
x = 10
y = 10
z = 20
print("Identity Operators:") # `is` and `is not` are used to compare the memory location of the objects.
print("is:", x is y) # True
print("is not:", x is not z) # True