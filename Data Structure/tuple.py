# A tuple is a collection which is ordered and unchangeable.

tuple1 = (1, 2, 3, 4, 5)  # Tuple with same data types
tuple2 = ("a", "b", "c", "d", "e")  # Tuple with same data types
tuple3 = (1, "a", 2, "b", 3, "c")  # Tuple with different data types
tuple4 = (1, 2, (3, 4, 5), 6, 7)  # Nested Tuple
print(type(tuple1))  # Output: <class 'tuple'>

print(tuple1, tuple2, tuple3, tuple4)

# Length of the tuple using len() function
print("Length of tuple1: ", len(tuple1))  # Output: 5
print("Length of tuple2: ", len(tuple2))  # Output: 5
print("Length of tuple3: ", len(tuple3))  # Output: 6
print("Length of tuple4: ", len(tuple4))  # Output: 5

# Concatenation
tuple5 = tuple1 + tuple2
print(
    "Concatenation of tuple1 and tuple2: ", tuple5
)  # Output: (1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e')

tuple6 = tuple4 + tuple3
print(
    "Concatenation of tuple4 and tuple3: ", tuple6
)  # Output: (1, 2, (3, 4, 5), 6, 7, 1, 'a', 2, 'b', 3, 'c')

# Repetition
tuple7 = tuple1 * 3
print(
    "Repetition of tuple1: ", tuple6
)  # Output: (1, 2, (3, 4, 5), 6, 7, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Indexing
print("Character Index", tuple1[0])  # Output: 1
print("Character Index", tuple2[2])  # Output: c
print("Character Index", tuple3[-1])  # Output: c
print("List Index", tuple4[2])  # Output: (3, 4, 5)
print("List Index", tuple4[2][1])  # Output: 4

# Slicing
print("Slicing", tuple1[0:4])  # Output: (1, 2, 3, 4)
print("Slicing", tuple2[1:])  # Output: ('b', 'c', 'd', 'e')
print("Slicing", tuple4[:3])  # Output: (1, 2, (3, 4, 5))
print("Slicing", tuple3[-3:-1])  # Output: (2, 'b')

# Functions
print("Count: ", tuple4.count(4))  # Output: 1
print("Index: ", tuple2.index("d"))  # Output: 3

# Tuple to List
list1 = list(tuple1)
print("Tuple to List: ", list1)  # Output: [1, 2, 3, 4, 5]

# Tuple to Dictionary
dict1 = dict(tuple3)
print("Tuple to Dictionary: ", dict1)  # Output: {1: 'a', 2: 'b', 3: 'c'}
