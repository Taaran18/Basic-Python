# A list is a data structure that is a mutable, or changeable, ordered sequence of elements.
# Each element or value that is inside of a list is called an item.

list1 = [1, 2, 3, 4, 5]  # List with same data types
list2 = ["a", "b", "c", "d", "e"]  # List with same data types
list3 = [1, "a", 2, "b", 3, "c"]  # List with different data types
list4 = [1, 2, [3, 4, 5], 6, 7]  # Nested List
print(type(list1))  # Output: <class 'list'>

print(list1, list2, list3, list4)

# Length of the list using len() function
print("Length of list1: ", len(list1))  # Output: 5
print("Length of list2: ", len(list2))  # Output: 5
print("Length of list3: ", len(list3))  # Output: 6
print("Length of list4: ", len(list4))  # Output: 5

# Concatenation
list5 = list1 + list2
print(
    "Concatenation of list1 and list2: ", list5
)  # Output: [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']

list6 = list4 + list3
print(
    "Concatenation of list4 and list3: ", list6
)  # Output: [1, 2, [3, 4, 5], 6, 7, 1, 'a', 2, 'b', 3, 'c']

# Repetition
list7 = list1 * 3
print(
    "Repetition of list1: ", list6
)  # Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Indexing
print("Character Index", list1[0])  # Output: 1
print("Character Index", list2[2])  # Output: c
print("Character Index", list3[-1])  # Output: c
print("List Index", list4[2])  # Output: [3, 4, 5]
print("List Index", list4[2][1])  # Output: 4

# Slicing
print("Slicing", list1[0:4])  # Output: [1, 2, 3, 4]
print("Slicing", list2[1:])  # Output: ['b', 'c', 'd', 'e']
print("Slicing", list4[:3])  # Output: [1, 2, [3, 4, 5]]
print("Slicing", list3[-3:-1])  # Output: [2, 'b']

# Functions
print("Append: ", list1.append(6))  # Output: [1, 2, 3, 4, 5, 6]
print("Extend: ", list1.extend(list2))  # Output: ['a', 'b', 'c', 'd', 'e']
print("Insert: ", list1.insert(2, 7))  # Output: [1, 2, 7, 3, 4, 5, 6]
print("Sort: ", sorted(list1))  # Output: [1, 2, 3, 4, 5, 6]
print("Sort: ", sorted(list2))  # Output: ['a', 'b', 'c', 'd', 'e']

print("Sort: ", sorted(Reverse=True))  # Output: [6, 5, 4, 3, 2, 1]
print("Reverse: ", list3[3:2:1])  # Output: ['b']
print("Reverse: ", list2[::-1])  # Output: ['e', 'd', 'c', 'b', 'a']

print("Pop: ", list2.pop())  # Output: e
print("Remove: ", list4.remove(3))  # Output: None
print("Count: ", list4.count(4))  # Output: 1
print("Index: ", list2.index("b"))  # Output: 1
print("Clear: ", list2.clear())  # Output: None

# List to Tuple
tuple1 = tuple(list1)
print("List to Tuple: ", tuple1)  # Output: (1, 2, 7, 3, 4, 5, 6)

# List to Dictionary
dict1 = dict(list3)
print("List to Dictionary: ", dict1)  # Output: {1: 'a', 2: 'b', 3: 'c'}
