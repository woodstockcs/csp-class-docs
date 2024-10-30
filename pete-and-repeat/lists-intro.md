---
title: Lists Intro
parent: Pete and Repeat
nav_order: 4
layout: default
---

# Lists Intro

Where we learn about:

- What lists are and why we use them
- Creating lists and accessing elements (indexing)
- Basic list operations (length, accessing items)

# Part 1 Warmup (5 minutes)

## 1.1

```python
for i in range(4):
    print(i, "Mississippi")
```

a. How many times does this loop run?

b. What's the first value of i?

c. What's the last value of i?

## 1.2

```python
x = 5
y = x + 2
x = 7
print(y)
```

a. What value is in y when it gets printed?

b. Does changing x after setting y affect y's value?

## 1.3

A few lessons ago, we looked at this problem:

```python
# We want to say hello to 5 friends:
# Alice, Bob, Charlie, Diana, and Eddie

count = 0
while count < 5:
    print("Hello", "???")
    count = count + 1
```

Then we learned a way to solve it using `for ... in:`. How would you fill in the blanks to make the program below work?

```python
friends = ["Alice", "Bob", "Charlie", "Diana", "Eddie"]

for friend in ______:
    print("Hello", _____)
```

# Part 2. Predictions (15 minutes)

## 2.1

```python
# Program A
numbers = [1, 2, 3]
print("First number:", numbers[0])
print("All numbers:", numbers)

# Output:
# First number: 1
# All numbers: [1, 2, 3]
```

```python
# Program B
names = ["Al", "Bob", "Cal"]
print("Winning name:", names[2])
print("All names:", names)

# Output:
# Winning name: Cal
# All names: ['Al', 'Bob', 'Cal']
```

**Question:** What will Program C output?

```python
# Program C
grades = ["A", "B", "C"]
print("Uhhhh:", grades[0])
print("Grades:", grades)
print("OK:", grades[1])

# Output:
# ...
```

## 2.2

```python
# Program A
nums = [10, 20, 30, 40]
print("Last:", nums[-1])
print("Second to last:", nums[-2])
# Output:
# Last: 40
# Second to last: 30
```

```python
# Program B
words = ["apple", "banana", "cherry"]
print("Last fruit:", words[-1])
print(words[-2])
# Output:
# Last fruit: cherry
# banana
```

**Question:** What will Program C output?

```python
# Program C
colors = ["red", "green", "blue"]
print(colors[-1])
print(colors[-3])
# Output:
# ...
```

## 2.3

```python
# Program A
scores = [75, 80, 85]
print("Before:", scores)
scores[0] = 95
print("After:", scores)
# Output:
# Before: [75, 80, 85]
# After: [95, 80, 85]
```

```python
# Program B
names = ["Al", "Bob", "Cal"]
print("Before:", names)
names[1] = "Ben"
print("After:", names)
# Output:
# Before: ['Al', 'Bob', 'Cal']
# After: ['Al', 'Ben', 'Cal']
```

**Question:** What will Program C output?

```python
# Program C
pets = ["cat", "dog", "fish"]
print("Before:", pets)
pets[2] = "bird"
print("After:", pets)
# Output:
# ...
```

## 2.4

```python
# Program A
fruits = ["apple", "banana"]
print("Is apple included?", "apple" in fruits)
print("Is orange included?", "orange" in fruits)
# Output:
# Is apple included? True
# Is orange included? False
```

```python
# Program B
nums = [1, 2, 3]
print("Is 2 in the list?", 2 in nums)
print(4 in nums)
# Output:
# Is 2 in the list? True
# False
```

**Question:** What will Program C output?

```python
# Program C
colors = ["red", "blue"]
print("red" in colors)
print("green" in colors)
# Output:
# ...
```

# Part 3. Explanation (15 minutes)

### A list is an ordered collection of items

- Items can be numbers, strings, or other types
- Items are stored in sequence
- Items can be accessed by their position (index)

### List indexing

- Indexes start at 0
- Last item is at length-1
- Negative indexes count from the end (-1 is last item)

### Basic list operations

- Create: `my_list = [item1, item2, item3]`
- Access: `my_list[index]`
- Modify: `my_list[index] = new_value`
- Length: `len(my_list)`
- Check membership: `if item in my_list:`

# Part 4. Practice

Create a file called `lists-intro.py` and do the following coding exercises in it.

## 4.1 Creating Lists
- Create a list called `weekdays` containing the names of the five weekdays.
- Then print the list.
- Then use list indexing to print a sentence that tells us your favorite weekday.

## 4.2 Accessing Elements
```python
numbers = [10, 20, 30, 40, 50]
# Use indexing to print:
# First number
# Last number
# Middle number
```

## 4.3 Working with Lists
```python
temperatures = [72, 75, 73, 71, 74]
# Print the number of temperatures
# Print whether 76 is in the list
# Change the last temperature to 77
```

## 4.4 Challenge
```python
# Create a list representing a tic-tac-toe board
# ["-", "-", "-"]
# ["-", "X", "-"]
# ["-", "-", "-"]
# Then change the center position to "O"
```

**Bonus Challenge:** Print the board so it looks like this:
```
- - -
- O -
- - -
```
