# A dictionary is a collection which is unordered, changeable and indexed.

dict1 = {"Name": "Zara", "Age": 7, "Class": "First"}
dict2 = {"Section": "A", "Roll_no": 12, "Subject": "Maths"}
print(type(dict1))  # Output: <class 'dict'>

print(dict1, dict2)

# Length of the dictionary using len() function
print("Length of dict1: ", len(dict1))  # Output: 3
print("Length of dict2: ", len(dict2))  # Output: 3

# Concatenation
dict1.update(dict2)
print(
    "Concatenation of dict1 and dict2: ", dict1
)  # Output: {'Name': 'Zara', 'Age': 7, 'Class': 'First', 'Section': 'A', 'Roll_no': 12, 'Subject': 'Maths'}

# Indexing
print("Character Index", dict1["Name"])  # Output: Zara
print("Character Index", dict2["Subject"])  # Output: Maths

# Functions
print(
    "Keys: ", dict1.keys()
)  # Output: dict_keys(['Name', 'Age', 'Class', 'Section', 'Roll_no', 'Subject'])
print(
    "Values: ", dict1.values()
)  # Output: dict_values(['Zara', 7, 'First', 'A', 12, 'Maths'])
print(
    "Items: ", dict1.items()
)  # Output: dict_items([('Name', 'Zara'), ('Age', 7), ('Class', 'First'), ('Section', 'A'), ('Roll_no', 12), ('Subject', 'Maths')])
print("Get Value: ", dict1.get("Name"))  # Output: Zara
print("Pop: ", dict1.pop("Subject"))  # Output: Maths
print("Pop Item: ", dict1.popitem())  # Output: ('Roll_no', 12)

# Dictionary to List
list1 = list(dict1)
print("Dictionary to List: ", list1)  # Output: ['Name', 'Age', 'Class', 'Section']

# Dictionary to Tuple
tuple1 = tuple(dict1)
print("Dictionary to Tuple: ", tuple1)  # Output: ('Name', 'Age', 'Class', 'Section'
