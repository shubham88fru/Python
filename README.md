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