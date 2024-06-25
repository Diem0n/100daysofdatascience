
# Day 1: Python, Visualization, and Linear Algebra

## Python

### Default Dict from Collections
The `defaultdict` is a subclass of the built-in `dict` class. It overrides one method and adds one writable instance variable. The advantage of using `defaultdict` is that it initializes with a default value if the key has not been set yet.

```python
from collections import defaultdict

# Example usage
dd = defaultdict(int)
dd['a'] += 1
print(dd['a'])  # Output: 1
print(dd['b'])  # Output: 0 (default value)
```

### Counter from Collections
`Counter` is a dictionary subclass for counting hashable objects. It's an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

```python
from collections import Counter

# Example usage
c = Counter('gallahad')
print(c)  # Output: Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
```

### Sorting with key=abs for Absolute Values
You can sort a list of numbers based on their absolute values using the `key` parameter.

```python
numbers = [10, -1, 2, -5, 7]
sorted_numbers = sorted(numbers, key=abs)
print(sorted_numbers)  # Output: [ -1, 2, -5, 7, 10 ]
```

### List Comprehensions
List comprehensions provide a concise way to create lists.

```python
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Generators and Lazy Yielding
Generators are functions that return an iterable set of items, one at a time, in a special way.

```python
def generate_squares(n):
    for i in range(n):
        yield i ** 2

squares = generate_squares(10)
for square in squares:
    print(square)
```

### Randomness
- `randrange`
- `choice` (with replacement)
- `shuffle`
- `sample` (without replacement)

```python
import random

# randrange
print(random.randrange(10))  # Random number between 0 and 9

# choice
print(random.choice(['a', 'b', 'c']))  # Random element from the list

# shuffle
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)  # Shuffled list

# sample
print(random.sample([1, 2, 3, 4, 5], 3))  # Three random elements from the list
```

### Regular Expressions
Regular expressions provide a powerful way to search and manipulate strings.

```python
import re

# Example usage
pattern = re.compile(r'\d+')
match = pattern.search('The year is 2024')
print(match.group())  # Output: 2024
```

### Functools.partial to Curry Functions
`functools.partial` allows you to fix a certain number of arguments of a function and generate a new function.

```python
from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))  # Output: 10
```

### Enumerate
`enumerate` adds a counter to an iterable and returns it as an enumerate object.

```python
items = ['a', 'b', 'c']
for index, item in enumerate(items):
    print(index, item)
```

### Map, Reduce, Filter, Zip
- `map` applies a function to all the items in an input list.
- `reduce` applies a rolling computation to sequential pairs of values in a list.
- `filter` creates a list of elements for which a function returns true.
- `zip` combines two or more iterables.

```python
from functools import reduce

# map
print(list(map(lambda x: x**2, [1, 2, 3, 4])))  # Output: [1, 4, 9, 16]

# reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))  # Output: 10

# filter
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))  # Output: [2, 4]

# zip
a = [1, 2, 3]
b = ['a', 'b', 'c']
print(list(zip(a, b)))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
```

### Args and Kwargs
Using `*args` and `**kwargs` allows you to pass a variable number of arguments to a function.

```python
def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo(1, 2, 3, a=4, b=5)
```

## Visualization (matplotlib.pyplot)

### Line Plot
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()
```

### Bar Plot
```python
plt.bar(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Plot')
plt.show()
```

### Histogram
```python
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=5)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
```

### Scatter Plot
```python
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()
```

## Linear Algebra

### Vectors
Vectors can be represented as lists in Python.

```python
import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Vector addition
print(v1 + v2)  # Output: [5 7 9]

# Dot product
print(np.dot(v1, v2))  # Output: 32
```

### Matrices
Matrices can be represented using 2D lists or NumPy arrays.

```python
# Matrix representation
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix addition
print(matrix1 + matrix2)  # Output: [[ 6  8]
                         #          [10 12]]

# Matrix multiplication
print(np.dot(matrix1, matrix2))  # Output: [[19 22]
                                 #          [43 50]]
```
