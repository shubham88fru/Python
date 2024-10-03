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

# OOPS

```python
# a class
class Car:
    pass


# an object of class
audi = Car()
bmw = Car()


# constructor
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age=age

dog1=Dog("Maxi", 2)
dog2=Dog("Reilly", 4)

# instance methods
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!")

dog3=Dog("Sammy", 5)
dog3.bark()

# Inheritance
class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
    
    def drive(self):
        print(f"The person will drive the {self.enginetype} car.")

class BMW(Car): # BMW inheriting from Car
    def __init__(self, windows, doors, enginetype, is_selfdriving):
        super().__init__(windows, doors, enginetype) # call parent's const.
        self.is_selfdriving=is_selfdriving
    
    
    def selfdriving(self):
        print(f"BMW supports self driving: {self.is_selfdriving}")

bmw1=BMW(4,5,"electric",True)
bmw1.selfdriving()

# Python supports multiple inheritance
class Animal:
    def __init__(self, name):
        self.name=name
    
    def speak(self):
        print("Subclasses must implement this method")

class Pet:
    def __init__(self, owner):
        self.owner=owner

class Dog(Animal, Pet): # Dog inheriting from Animal and Pet.
    def __init__(self, name, owner):
        Animal.__init__(self, name) # instead of super.__init__
        Pet.__init__(self, owner) # instead of super.__init__
    
    def speak(self): # overrides speak from Animal super class.
        return f"{self.name} says woof!"

dog=Dog("Buddy", "Krish")
dog.speak()

# Polymorphism (achieved through method overriding and abstract classes.)
# Method overriding -> Method overriding allows a child class to provide a 
# specific implementation of a method that is already defined in its parent class.
class Animal:
    def speak(self):
        return "Sound of animal"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())

def animal_speak(animal):
    print(animal.speak())

animal_speak(dog)
animal_speak(cat)

# Creating abstract classes.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self): # implementation needs to be in subclasses
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

class MotorCycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started."

car = Car()
motorcycle = MotorCycle()

# Magic methods.
# Magic methods in python, also known as dunder methods (double underscore
# methods), are special methods that start and end with double underscores.
# These methods enable you to define the behavior of objects for built-in
# operations, such as arithmetic operations, comparisons, and more.

# Magic methods are predefined methods in Python that you can override to
# change the behavior of your objects. Some common magic methods include:
# 1. __init__: Initializes a new instance of a class.
# 2. __str__: Returns a string representation of an object.
# 3. __repr__: Returns an official string representation of an object.
# 4. __len__: Returns the length of an object.
# 5. __getitem__: Gets an item from a container.
# 6. __setitem__: Sets an item in a container.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): # override the inbuilt to string method.
        return f"{self.name}, {self.age} years old."

person=Person("Shubham", 28)
print(person) # --> Shubham, 28 years old.

# Operator overloading.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y=y

    def __add__(self, other): # overload the `+` operator
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other): # overload the `-` operator
        return Vector(self.x-other.x, self.y-other.y)

    def __mul__(self, other): # overload the `*` operator
        return Vector(self.x*other.x, self.y * other.y)

    def __eq__(self, other): # overload the `==` operator
        return self.x==other.x and self.y==other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1+v2) # --> Vector(6, 8)
```

# Advanced Python

```python
# Iterators
# Iterators provide a way to access elements of a collection sequentially
# without exposing the underlying structure.
my_list = [1, 2, 3, 5, 6]
iterator = iter(my_list)
next(iterator) # --> 1
next(iterator) # --> 2

# Generators
#  are a simpler way to creat iterators. They use the yield keyword
# to produce a series of values lazily, which means they generate values on the
# fly and do not store them in memory.
def square(n):
    for i in range(3):
        yield i**2

gen = square(3)
next(gen) # --> 0
next(gen) # --> 1
next(gen) # --> 4

# one usecase of generators - Reading a large file.
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

            
# Function copy
def welcome():
    return "Welcome to the advanced python course"

welcome()
wel=welcome()
print(wel())
del welcome
print(wel()) # still works even after deleting welcome.

# closures
def main_welcome():
    msg="Welcome"
    def sub_welcome_method():
        print(f"Welcome {msg} to the advanced python course.")
        print("Please learn these concepts properly.")
        
    return sub_welcome_method

# Decorators
# Allows one to modify the behavior of a function or class method. They are
# commonly used to add functionality to functions or methods without modifying
# their actual code.

def execute_func(func):
    func()


# The function print_me will be passed as an argument to
# execute_fuc
@execute_func
def print_me(str):
    print(str)

def my_decorator(func):
    def wrapper():
        print("Before the func is called..")
        func()
        print("After the func is called..")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the func is called..
# Hello!
# After the func is called..

# Decorator with arguments.
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello")

say_hello()
# Output:
# Hello
# Hello
# Hello
```

# Data Analysis with Python
## numpy
```python
# Numpy is a fundamental library for scientific computing in python. It provides
# support for arrays and matrices, along with a collection of mathematical functions
# to operate on these data structures.
import numpy as np

# create array using numpy
# creating a 1D array.
arr1 = np.array([1, 2,3,4,5])
print(arr1.ndim) # number of dimensions --> 1
print(arr1) # [ 1 2 3 4 5 ]
print(type(arr1))
print(arr1.shape) # (5,) --> a single dimension array with 5 elements.

arr2 = np.array([[1,2,3,4,5]])
print(arr2.ndim) # 2
arr2.reshape(1,5) # 1 row and 5 columns.

arr3 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr3.size) # m*n --> 10
print(arr3.shape) # (2, 5) --> 2 rows and 5 columns.

arr4 = np.arange(0, 10, 2) # from 0 to 10 with steps size of 2.
print(arr4) # [0, 2, 4, 6, 8, 10]
arr4.reshape(5, 1) # 5 rows and 1 column.

arr5 = np.ones((3,4)) # a 3*4 np array with all ones.

arr6 = np.eye(3) # create a 3*3 identity matrix.

# Numpy vectorized operations
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([10,20,30,40,50])
print(f"Element wise addition: {arr1 + arr2}") # [11 22 33 44 55]
print(f"Element wise subtraction: {arr1 - arr2}") # [-9 -18 -27 -36 -45]
print(f"Element wise mult: {arr1 * arr2}") # [10 40 90 160 250]
print(f"Element wise division: {arr1 / arr2}") # [0.1 0.1 0.1 0.1 0.1]

# Universal functions (will apply to each element of the array)
arr = np.array([2,3,4,5,6])
print(np.sqrt(arr))
print(np.exp(arr))
print(np.sin(arr))
print(np.log(arr))

# Array slicing and indexing
arr=np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print("Array: \n", arr) # 3*4 np array.
print(arr[0][0]) # 1
print(arr[0:2]) # 0th and 1st rows --> [[1 2 3 4] [5 6 7 8]]
print(arr[1:]) # everything from 2nd row --> [[5,6,7,8] [9,10,11,12]]
print(arr[1:, 1:3]) # [[6 7] [10 11]]

# everything that matches row=1+ and column=2+
print(arr[1:, 2:]) # --> [[7 8] [11 12]]

# Statistical operations
data = np.array([1,2,3,4,5])
mean = np.mean(data) # calculates mean
std_dev = np.std(data) # calculates standard deviation
normalized_data = (data-mean)/std_dev # Normalize the data
print("Normalized data: ", normalized_data)

# Logical operations
data = np.array([1,2,3,4,5,6,7,8,9,10])
print(data[data>5]) # all elements of the array that are greater than 5.
```

## pandas
```python
# Pands is a data manipulation library in Python, widely used for data analysis
# and data cleaning. It provides two primary data structures: Series and DataFrame.
# A series is a one-dimensional array-like object, while a DataFrame is a two-dimensional,
# size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).

# Series
# A pandas series is a one-dimensional array-like object that can hold any data type.
# It is similar to a column in a table.
import pandas as pd
data=[1,2,3,4,5]
series=pd.Series(data) # series from array/list
print("Series \n", series)

# create a series from dictionary.
data={'a':1, 'b': 2, 'c': 3}
series_dict=pd.Series(data)
print(series_dict)

# Dataframe
# create a Dataframe from a dictionary of list.

data={
    'Name': ['Krish', 'John', 'Jack'],
    'Age': [25, 30, 45],
    'City': ['Bangalore', 'New York', 'Tempe']
}
df = pd.DataFrame(data)
print(df)
# output
#######################
#   Name    Age     City
# 0 Krish   25  Bangalore
# 1 John    30  New York
# 2 Jack    45  Tempe
#######################
print(type(df))

# dataframe to numpy array.
import numpy as np
narr = np.array(df)

# Create a Data frame from a list of Dictionaries
data=[
    { 'Name': 'Krish', 'Age': 32, 'City': 'Bangalore' },
    { 'Name': 'John', 'Age': 34, 'City': 'Bangalore' },
    { 'Name': 'Bappy', 'Age': 32, 'City': 'Bangalore' },
    { 'Name': 'Jack', 'Age': 32, 'City': 'Bangalore' }
]
df = pd.DataFrame(data)
print(df)
# output
#########################
#   Name    Age     City
# 0 Krish   32  Bangalore
# 1 John    34  Bangalore
# 2 Bappy   32  Bangalore
# 3 Jack    32  Bangalore
#########################

# reading a csv file
df=pd.read_csv('sales_data.csv')
df.head(5) # table of first 5 rows.
df.tail(5) # last 5 records.

name_column = df['Name'] # read the 'Name' column. Returns a series (column).

# loc[] is primarily used for label-based indexing. 
# It selects data based on the labels of rows and columns.
row=df.loc['row_label'] # Select row by label

multi=df.loc[:, ['col1', 'col2']] # Select multiple columns

slic=df.loc['row1':'row3', 'col1':'col3'] # Slice rows and columns by label

bindex=df.loc[df['column'] > 5] # Boolean indexing

# iloc[] is used for integer-based indexing. 
# It selects data based on the integer position of rows and columns.
iloc_1=df.iloc[0] # Select row by integer position

iloc_2=df.iloc[:, [0, 2]] # Select multiple columns by position

iloc_2=df.iloc[0:3, 0:3] # Slice rows and columns by position

iloc_2=df.iloc[[1, 3, 5], [2, 4]] # Select specific rows and columns

df.at[1, 'Age'] # get the value from 1st row's 'Age' column.

# adding a new column to a data frame.
df['Salary'] = [50000, 60000, 70000] # adds a salary column.

# remove a row
df.drop(0,inplace=True) # drop 0th row.
df.drop('Salary', axis=1,inplace=True) # drop 'Salary' column and mutate the df.

df['Age'] = df['Age']+1 # Increment each value in df column by 1.

# Data manipulation and analysis with Pandas.
import pandas as pd

df=pd.read_csv("data.csv")

# fetch first 5 rows.
df.head(5)

# last five rows.
df.tail(5)

# get stats - count, mean, median etc
df.describe()

# Handling missing values in data.
df.isnull() # prints the df, where each cell if either True/False depending if its empty.

# fill the missing values in any cell, with a default value.
df.fillna(0) # set inplace=True for inplace change.

# fill missing values with mean of the column.
df["Sales_fillNA"] = df["Sales"].fillna(df['Sales'].mean()) # fill any missing values in sales column, with the mean of that column.

# Renaming a column.
df = df.rename(columns={'Date': 'Sale Date'}) # Rename 'Date' column to 'Sale Date'

# change datatype of a column.
df['value_new'] = df['value'].astype(float) # change datatype of value column to float.

# Apply some transformation (function) to a column.
df['New Value'] = df['Value'].apply(lambda x: x*2) # multiple each value of 'Value' column with 2.

# Data aggregating and grouping
grouped_mean = df.groupby('Product')['Value'].mean() # group by the products and for each group, find the mean of "value" column.

grouped_sum = df.groupby(['Product', 'Region'])['Value'].sum() # group by 'Product' and 'Region' column and for each group, find the sum of 'value' column.

# apply multiple aggregate functions
grouped_agg = df.groupby('Region')['Value'].agg(['mean', 'sum', 'count']) # group by 'Region' and for each group calculate mean, sum and count of 'value' column.

# Merging and joining data frames.
df1 = pd.DataFrame({'Key': ['A', 'B', 'C'], 'Value1': [1, 2, 3]})
df2 = pd.DataFrame({'Key': ['A', 'B', 'C'], 'Value2': [4, 5, 6]})

pd.merge(df1, df2, on="Key", how="inner") # inner join on key column.

# Reading data from various sources using pandas. (read_* functions)
json='' # some json
df=pd.read_json(json) # read the json and convert to a df.
json=df.to_json() # convert the df to json
json=df.to_json(orient="records")

# Matplotlib
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[1,4,9,16,25]

# create a line plot
plt.plot(x, y) # plot a X, Y line graph.
plt.xlabel('X axis') # x axis label
plt.ylabel('Y axis') # y axis label
plt.title("Basic line plot") # title of the entire plot.
plt.show() # display the plot.

plt.plot(x, y, color="red", linestyle="--")

# Bar plot
categories=['A', 'B', 'C', 'D', 'E']
values=[5,7,3,8,6]

# create a bar plot
plt.bar(categories, values, color='purple')

df.plot(kind='bar', color="teal") # plot a bar plot from a dataframe.

# Histogram
data = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
plt.hist(data, bins=5)

# scatter plot
x = [1,2,3,4,5]
y = [2,3,4,5,6]

plt.scatter(x,y,color="blue",marker="x")

# pie charts
labels=['A', 'B', 'C', 'D']
sizes=[30,20,40,10]
colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode=(0.1, 0, 0, 0)

plt.pie(sizes, labels, colors=colors)

# Visualizations using seaborn.
# Seaborn is a python visualization library based on matplotlib.
import seaborn as sns

# Basic plotting with seaborn
tips = sns.load_dataset('tips')

##scatter plot
import matplotlib.pyplot as plt
sns.scatterplot(x="total_bill", y='tip', data=tips)
plt.title("Scatter plot of total bill v/s tip") # using matplotlib alongside seaborn
plt.show()

# Line plot
sns.lineplot(x='size', y='total_bill', data=tips)
plt.title("Line plot of total bill by size")
plt.show()

# Categorical plots
# bar plots
sns.barplot(x='day', y='total_bill', data=tips)
plt.title("Bar plot of total bill by day")
plt.show()

# Box plot
sns.boxplot(x="day", y="total_bill", data=tips)

# Violin plot
sns.violinplot(x='day', y='total_bill', data=tips)

# histogram
sns.histplot(tips['total_bill'], bins=10, kde=True)

# kde plot
sns.kdeplot(tips['total_bill'], fill=True)

# Pair plot
sns.pairplot(tips) # builds a plot for every pair of columns.

# Heatmap
corr=tips[['total_bill', 'tip', 'size']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
```

# Logging
```python
import logging

# configuring the logging more.
logging.basicConfig(
    filename='app.log', # write log to this file.
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# log a message
logging.debug("This is a debug message.")
logging.info("This is a info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")
```