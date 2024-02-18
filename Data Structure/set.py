# Set is a collection of unordered and unindexed elements. It is written in curly brackets {}.

set1 = {1, 2, 3, 4, 5}
set2 = {"a", "b", "c", "d", "e"}
set3 = {1, "a", 2, "b", 3, "c"}
set4 = {1, 2, 3, 4, 5, 6, 7}
print(type(set1))  # Output: <class 'set'>

print(set1, set2, set3, set4)

# Length of the set using len() function
print("Length of set1: ", len(set1))  # Output: 5
print("Length of set2: ", len(set2))  # Output: 5
print("Length of set3: ", len(set3))  # Output: 6
print("Length of set4: ", len(set4))  # Output: 7

# Concatenation or Union
set5 = set1.union(set2)
print(
    "Concatenation of set1 and set2: ", set5
)  # Output: {1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e'}

set6 = set4.union(set3)
print(
    "Concatenation of set4 and set3: ", set6
)  # Output: {1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c'}

# Intersection
set7 = set1.intersection(set2)
print("Intersection of set1 and set2: ", set7)  # Output: set()

set8 = set4.intersection(set3)
print("Intersection of set4 and set3: ", set8)  # Output: {1, 2, 3}

# Difference
set9 = set1.difference(set2)
print("Difference of set1 and set2: ", set9)  # Output: {1, 2, 3, 4, 5}

set10 = set4.difference(set3)
print("Difference of set4 and set3: ", set10)  # Output: {4, 5, 6, 7}

# Functions
print("Add: ", set1.add(6))  # Output: {1, 2, 3, 4, 5, 6}
print("Remove: ", set1.remove(6))  # Output: {1, 2, 3, 4, 5}
print("Pop: ", set1.pop())  # Output: 1
print("Discard: ", set3.discard(3))  # Output: {1, 2, 'a', 'b', 'c'}
print("Is Disjoint: ", set4.isdisjoint(set3))  # Output: False
print("Is Subset: ", set1.issubset(set4))  # Output: True
print("Is Superset: ", set4.issuperset(set1))  # Output: True

# Set to List
list1 = list(set1)
print("Set to List: ", list1)  # Output: [1, 2, 3, 4, 5]

# Set to Tuple
tuple1 = tuple(set1)
print("Set to Tuple: ", tuple1)  # Output: (1, 2, 3, 4, 5)

# Set to Dictionary
dict1 = dict.fromkeys(set3)
print(
    "Set to Dictionary: ", dict1
)  # Output: {1: None, 2: None, 3: None, 'a': None, 'b': None, 'c': None}
