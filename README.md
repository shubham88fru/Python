# Lists
```python
lst = [] # empty list
lst3=list() #empty list
print(type(lst))

names = ["Shubham", "Singh"]
mixed_list = [1, "Hello", 3.14, True]

# Accessing list elements
fruits=["apple", "banana", "cherry", "kiwi", "guava"]
print(fruits[0]) # first element
print(fruits[-1]) # last element

# slicing
print(fruits[1:]) # all fruits from index 1 till end of list -> ["banana", "cherry", "kiwi", "guava"]
print(fruits[1:3]) # all fruits from index 1 till 2 (note: 3 is not included). -> ["banana", "cherry"]
print(fruits[-1:]) # all fruits from the last index to the end of list. -> ["guava"]

# Modifying the list elements.
fruits[1] = "watermelon"
print(fruits)

# List methods
fruits.append("orange") # Add "orange" to the end of list.
fruits.insert(1, "mango") # insert "mango" at index 1.
fruits.remove("banana") # remove the first occurrence of "banana".
last_fruit = fruits.pop() # remove the last fruit and return.
fruits.index("cherry") # return the index of "cherry" in the list.
fruits.count("banana") # count the occurrences of "banana" in the list.
fruits.sort() # sort the fruits list.
fruits.clear() # remove all items from the list.

# More on slicing.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:5])
print(fruits[:5]) # all elements before the 4th index (note 5 is not included) till the first element -> [1, 2, 3, 4, 5] 
print(fruits[::]) # all the elements -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(fruits[::-1]) # all the elements from the last -> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(fruits[::2]) # starting from the first element (index 0) all elements with step size 2. -> [1, 3, 5, 7, 9]

# Iterating over lists.
for fruit in fruits:
    print(fruit)

# Iterating with index
for index, number in enumerate(numbers):
    print(index, number)

# List comprehension
# Basic template: [expression for item in iterable]
# With some conditionals: [expression for item in iterable if condition]
# Nested list comprehension: [expression for item1 in iterable1 for item2 in iterable2]
lst = []
for x in range(10):
    lst.append(x**2)

sqrs = [x**2 for x in range(10)] # Basic

even_sqrs = [x**2 for x in range(10) if x%2==0] # with condition that only even numbers considered for squaring. 

lst1=[1, 2, 3, 4]
lst2=['a', 'b', 'c', 'd']
pair=[[i, j] for i in lst1 for j in lst2] # Nested -> [[1, 'a], [1, 'b'], [1, 'c'], [1, 'd'], [2, 'a'], [2, 'b'], ....]

# List comprehension with function calls.
words = ["hello", "world", "python", "list", "comprehension"]
lengths = [len(word) for word in words]
print(lengths) # [5, 5, 6, 4, 13]
```

# Tuples
```python
# Tuples are ordered collections of items that are immutable. They are similar to lists, but their immutability makes them different.
# Creating a tuple
empty_tuple = ()
print(empty_tuple) #()
print(type(empty_tuple))

lst = list()
print(type(lst))

tpl=tuple() # empty tuple
print(type(tpl))

lst_to_tuple=tuple([1, 2, 3, 4, 5, 6]) # convert list to tuple
print(lst_to_tuple) # (1, 2, 3, 4, 5, 6)

tuple_to_lst = list((1, 2, 3, 4, 5, 6)) # convert tuple to list
print(tuple_to_lst)

mixed_tuple=(1, "Hello world", 3.14, True)

# Accessing tuple elements
print(lst_to_tuple[0]) # first element of tuple -> 1
print(lst_to_tuple[-1]) # last element of tuple -> 6
print(lst_to_tuple[0:4]) # elements from index 0 to 3 (4 not included) -> (0, 1, 2, 3)
print(lst_to_tuple[::]) # all elements of tuple.
print(lst_to_tuple[::-1]) # all elements of tuple in reverse order.

# Tuple operations
concatenated_tuple = mixed_tuple + lst_to_tuple # concatenate two tuples -> (1, "Hello world", 3.14, True, 1, 2, 3, 4, 5, 6)
repeated_tuple = mixed_tuple * 3 # a tuple with mixed_tuple repeated 3 times.

# Immutable nature of tuples.
# Tuples are immutable, i.e. their elements cannot be changed once assigned.
lst=[1,2,3,4,5]
print(lst)

lst[1] = "shubham"
print(lst) #lists are immutable -> ["shubham", 2, 3, 4, 5]

lst_to_tuple[0] = 10 # error, tuple doesn't support assignment.

# Tuple methods.
print(lst_to_tuple.count(1)) # Number of times 1 is present in the tuple -> 1.
print(lst_to_tuple.index(3)) # Index at which 3 is present in the tuple -> 2.

# Packing and unpacking tuple
packed_tuple=1,"Hello",3.14 #packing a tuple
print(packed_tuple) # (1, "Hello", 3.14)

a, b, c = packed_tuple #unpacking a tuple
print(a, b, c) # 1 "Hello" 3.14

numbers=(1,2,3,4,5,6)
first,*middle,last=numbers # unpacking with *
print(first) # first=1
print(middle) # middle=[2,3,4,5]
print(last) # last=6

# Nested tuples
tpl=((1,2,3,4), (6,7,8,9), (1, "Hello", 3.14, "c"))
print(tpl[0][0:3]) # (1,2,3)
```

# Sets
```python
# create a set
my_set = { 1, 2, 3, 4, 5}
empty_set = set()
new_set = set([1, 2, 3, 4, 5]) # list to set.

# basic set operations
# Add/remove elements
my_set.add(7) # add 7 to the set.
my_set.remove(3) # remove 3 from the set.
my_set.discard(10) # remove if 10 is present, else just ignore.
my_set.clear() # clear the set.

# membership test
print(3 in my_set) # True
print(10 in my_set) # False

# Mathematical operations.
set1 = { 1, 2, 3, 4, 5, 6 }
set2 = { 4, 5, 6, 7, 8, 9 }

# union
union_set = set1.union(set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9 }

# Intersection
int_set = set1.intersection(set2) # { 4, 5, 6 }

set1.intersection_update(set2)
print(set1) # find intersection and update set1 with the result of intersection.

# Difference
diff_set = set1.difference(set2)
print(diff_set) # from set1, remove all the common elements present in set2 and return new set.

# Symmetric difference
symm_set = set1.symmetric_difference(set2)
print(symm_set) # combine unique elements of both the sets and return a new set.

# Set methods.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.issubset(set2)) # is set1 subset of set2? -> False
print(set1.issuperset(set2)) # is set2 a superset of set2? -> False
```

# Dictionaries
```python
# Creating dictionaries
empty_dict = {} # empty dictionary
empty_dict2 = dict() # empty dictionary

student = { "name": "krish", "age": 32, "grade": 'A' }
print(student)

# check if present
if "name" in student:
    print("Yes")

# Accessing dict elements
print(student['grade']) # A
print(student['age']) # 32

# Accessing using get() method
print(student.get("grade")) # 24
print(student.get("name")) # krish
print(student.get("last_name")) # None
print(student.get("last_name", "LNU")) # LNU

# Modifying dictionary elements.
# Dictionaries are mutable, so you can add, update or delete elements.
student['age'] = 33
student['country'] = "India"

# deleting a key
del student["grade"]

# Dictionary methods
dicts_keys = student.keys() # All keys of the dict. -> ['name', 'age', 'grade' ]
values = student.values() # All values of the dict. -> ["krish", 32, "A"]

# get k-v pairs
kv_pairs=student.items() # [('name', 'krish'), ('age', 32), ('grade', 'A')]

#shallow copy
student_cpy = student.copy() # creates a shallow copy of student.

# Iterating over dictionaries.
for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for k,v in student.items():
    print(f"{k}:{v}")

# Nested dictionaries
students = {
    "student1": { "name": "Krish", "age": 32 },
    "student2": { "name": "spider", "age": 35 },
}

# Access nested dictionary elements.
print(students["student1"]["name"])

# Iterating over nested dictionaries
for student_id, student_info in students.items():
    print(f"{student_id}:{student_info}")
    for k,v in student_info.items():
        print(f"{k}:{v}")

# Dictionary comprehension
squares = {f"{x}_sq": x**2 for x in range(5)} # square of nums from 0..4
square_even = {f"{x}_sq": x**2 for x in range(5) if x%2==0} # square of even nums in range 0..4

# merge two dicts
dict1={"a": 1, "b": 2}
dict2={"b": 3, "c": 4}
merged_dict = {**dict1, **dict2} # {"a":1, "b":3, "c": 4}
```

# Functions
```python
# syntax/template
def function_name(parameters):
    """Doc string"""
    #Body
    return 1

def even_or_odd(num):
    """checks if given num is odd or even"""
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")

even_or_odd(1)
even_or_odd(45)
even_or_odd(100)

# Default params
def greet(name="Guest"):
    print(f"Hello, {name}")

greet("Shubham") # Hello, Shubham
greet() # Hello, Guest

# Variable length args - Positional and Keyword args.
# 1. Positional args.
def print_numbers(*args): # args is similar to `rest` operator in JS. *args will capture all positional arguments in function call.
    for number in args:
        print(number)

print_numbers(1,2,3,4,5) # Solely positional args -> 1 2 3 4 5

# 2. Keyword args.
def print_details(**kwargs): # JS's rest operator for params with k-v pairs. **kwargs will capture all k-v pair type arguments in function call.
    for k,v in kwargs.items():
        print(k, v)

print_details(name="Shubham", age="32", country="India")

# Returning multiple values from a function
def some_func(a, b):
    return a*b,a

some_func(2, 3) # returns a tuple -> (6, 2)

# check if string is palindrome
def is_palindrome(s):
    s=s.lower().replace(" ", "")
    return s==s[::-1] #string reversing
```

# Lambda functions
```python
# Syntax/template -> lambda arguments: expression
def addition(a, b):
    return a+b

addition(1, 5) # 6

addition_lambda = lambda a, b: a+b
addition_lambda(2, 3) # 5

def even(num):
    if (num%2==0):
        return True
even(24) # True

even_lambda = lambda num: num%2==0
even_lambda(24) # True

# map() function
numbers=[1,2,3,4,5,6]
def square(num):
    return num**2

sq_lambda = lambda x: x**2
sq_nums = list(map(sq_lambda, numbers)) # [1,4,9,16,25,16]

# Map multiple iterables
numbers1 = [1,2,3]
numbers2 = [4,5,6]
added_numbers=list(map(lambda x,y: x+y, numbers1, numbers2)) # [5, 7, 9]

# Map to convert a list of strings to integers
str_numbers = ['1', '2', '3', '4', '5']
int_numbers = list(map(int, str_numbers)) # [1,2,3,4,5]

words=['apple', 'banana', 'cherry']
upper_words=list(map(str.upper, words))

def get_name(person):
    return person['name']

people=[
    {'name': 'Krish', 'age': 31},
    {'name': 'Jack', 'age': 33 }
]

names=list(map(get_name, people)) # ['Krish', 'Jack']

# filter() function
lst = [1,2,3,4,5,6,7,8,9,10]
even_nums = list(filter(even, lst)) # [2,4,6,8,10]
greater_than_five = list(filter(lambda x:x>5, lst)) # [6,7,8,9,10]
even_and_gt_5 = list(filter(lambda x:(x>5 and x%2==0), lst))
```

# Modules and Packages
```python
import math # importing a package in its entirety
math.sqrt(16) # 4

from math import sqrt, pi # import sqrt and pi from math module.
sqrt(16) # 4
sqrt(25) # 5
pi # 3.14

import math as m # set alias to math package.

from math import * # import everything from math module.

# Steps to create your own package and module.
# 1. Create a folder with any name (e.g. package)
# 2. Create a file named `__init__.py` inside the folder.
# 3. Doing step 2 declares the folder as a package and then each
# file inside the folder will be a module which can be imported like - 
# from package.my_module import hello
```

# Python standard library
```python
import random
print(random.randint(1, 10)) # random integer between 1 to 10.
print(random.choice(['apple', 'banana', 'mango', 'cherry'])) # random element from the list.

# file and directory access.
import os
print(os.getcwd()) # get current working directory.
os.mkdir("test_dir") # creat a folder named `test_dir` in the current folder.

# data serialization
import json
data = { 'name': 'Krish', 'age': 25 }
data_json_str = json.dumps(data) # convert the dict to json string rep.
print(data_json_str)

data_dict = json.loads(data_json_str) # convert json to dict rep.
print(data_dict)

# working with csv
import csv
# create a csv file and write two rows to it.
with open("example.csv", mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['Krish', 32])

# read each row of a csv file.
with open("example.csv", mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# dates
from datetime import datetime, timedelta
now = datetime.now()
print(now)
yesterday = now-timedelta(days=1)
print(yesterday)

# time
import time
print(time.time())
time.sleep(2) # sleep for 2 secs.
```

# File ops

```python
# open a file in read mode.
import os

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# read a file line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line)

# write to a file with overwriting.
with open("example.txt", "w") as file:
    file.write("Hello World!\n")
    file.write("this is a new line.")

# write to a file without overwriting (append mode)
with open("example.txt", "a") as file:
    file.write("Append operation took place")

# write a list of lines.
lst = ["first line", "second line", "third line"]
with open("examples.txt", "a") as file:
    file.writelines(lst)

# writing bytes
data = b"\x00\x01\x02\x03\x04"
with open("example.bin", "wb") as file:
    file.write(data)

# writing and then reading the file.
# `w+` mode open the file in read and write mode.
# If the file doesn't exist, its created and during writing,
# all its og content are overwritten.
with open("example.txt", "w+") as file:
    file.write("Hello word\n")
    file.write("This is a new line \n")

    file.seek(0)  # move the file cursor to start.
    content = file.read()
    print(content)

# create a new directory
new_dir = "package"
os.mkdir(new_dir)
print(f"Directory '{new_dir}' create")

import os
folders = os.listdir('.') # list all folders in current directory.
print(folders)

dir_name="folder"
file_name="file.txt"
full_path=os.path.join(dir_name,file_name)
print(full_path) # --> `folder\file.txt`
```

# Exception handling
```python

# try-except block
try:
    a=b
except:
    print("Exception occurred")

try:
    result=1/0
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)

try:
    num=int(input("Enter a number"))
    result=10/num
except ValueError as ve:
    print("This is not a valid number")
except ZeroDivisionError as ze:
    print("enter denominator greater than 0")

# Try except else block
try:
    num=int(input("Enter a num"))
    result=10/num
except ValueError as ve:
    print("That's not a valid number")
except ZeroDivisionError as ze:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    # This block executes only if 
    # there was no exception in the try block.
    print(f"This is the {result}")

# Try except else and finally
try:
    num=int(input("Enter a num"))
    result=10/num
except ValueError as ve:
    print("That's not a valid number")
except ZeroDivisionError as ze:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    # This block executes only if 
    # there was no exception in the try block.
    print(f"Only if no exception in try: {result}")
finally:
    # This block executes no matter what,
    # whether exception happens or not.
    print(f"No matter whether or not exception happens in finally.")

# Exception handling with file ops
file = None
try:
    file=open("example1.txt", "r")
    content=file.read()
    print(content)
except FileNotFoundError as fe:
    print("The specified file doesn't exist")
finally:
    if "file" is not None and not file.closed:
        file.close()
```