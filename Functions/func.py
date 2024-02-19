# Simple Function Code


def calc_sum(a, b):  # Function definition
    sum = a + b
    return sum


print(calc_sum(5, 10))  # Function call # Output: 15


# Built-in Functions
# print()
def print_function():
    print("Hello, world!")  # Output: Hello, world!


# len()
def len_function(input_list):
    length = len(input_list)
    return length


# type()
def type_function(input_var):
    data_type = type(input_var)
    return data_type


# range()
def range_function(start, stop, step):
    range_list = list(range(start, stop, step))
    return range_list


# Example usage
print_function()
my_list = [1, 2, 3, 4, 5]
print("Length of my_list:", len_function(my_list))  # Output: 5
my_var = 10
print("Type of my_var:", type_function(my_var))  #    Output: <class 'int'>
print("Range from 1 to 10 with step 2:", range_function(1, 10, 2))  # Output: [1, 3, 5, 7, 9]


# Default Parameters
def cal_prod(a=1, b=1):
    print(a * b)
    return a * b


cal_prod() # Output: 1
