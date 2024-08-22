## Lists

-------
# Intro
-------
```python
lst = [] # empty list
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