# A string is a sequence of characters. It can be a single character, word, sentence or a paragraph.

str1 = "This is a string"  # single line string
str2 = "This is also a string"
str3 = """This is a multiline string"""
str4 = "This is a string, \n with a comma."  # escape sequence (\n is used to print a new line.)
print(type(str1))  # Output: <class 'str'>

print(str1, str2, str3, str4)

# Length of the string using len() function
print("Length of str1: ", len(str1))  # Output: 16
print("Length of str2: ", len(str2))  # Output: 20
print("Length of str3: ", len(str3))  # Output: 23
print("Length of str4: ", len(str4))  # Output: 27

# Concatenation
str5 = str1 + str2
print(
    "Concatenation of str1 and str2: ", str5
)  # Output: This is a stringThis is also a string

str6 = str1 + " " + str2  # Adding space between two strings
print(
    "Concatenation of str1 and str2: ", str6
)  # Output: This is a string This is also a string

# Repetition
str6 = str1 * 3
print(
    "Repetition of str1: ", str6
)  # Output: This is a stringThis is a stringThis is a string

# Indexing
print("Character Index", str1[0])  # Output: T
print("Character Index", str3[5])  # Output: i
print("Character Index", str4[-5])  # Output: c

# Slicing
print("Slicing", str1[0:4])  # Output: This
print("Slicing", str2[5:])  # Output: is also a string
print("Slicing", str4[:12])  # Output: This is a st
print("Slicing", str3[-8:-2])  # Output: string

# Functions
print("Lowercase: ", str1.lower())  # Output: this is a string
print("Uppercase: ", str1.upper())  # Output: THIS IS A STRING
print("Replace: ", str1.replace("is", "was"))  # Output: Thwas was a string
print("Count: ", str1.count("is"))  # Output: 2
print("Find: ", str1.find("is"))  # Output: 2
print("Split: ", str1.split(" "))  # Output: ['This', 'is
print("Capitalize: ", str1.capitalize())  # Output: This is a string
print("Ends With: ", str1.endswith("string"))  # Output: True
