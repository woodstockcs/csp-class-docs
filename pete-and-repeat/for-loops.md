---
title: For Loops
parent: Pete and Repeat
nav_order: 2
layout: default
---

# For Loops

## Warm-up Questions (5 minutes)

### Question 1: Prior Knowledge - While Loops

```python
count = 0
while count < 3:
    print("Hello")
    count = count + 1
```

**Q:** How many times will this code print "Hello"?

### Question 2: Variable Updates

```python
friend = "Alice"
print("Hello", friend)
friend = "Bob"
print("Hello", friend)
```

**Q:** What will this code print?

### Question 3: The "Headache"

```python
# We want to say hello to 5 friends:
# Alice, Bob, Charlie, Diana, and Eddie

count = 0
while count < 5:
    # Yikes... how do we print the right name?
    print("Hello", "???")
    count = count + 1
```

**Q:** Using only what we know about while loops and variables, how could we solve this? What makes it awkward or difficult?

# Guided Code Reading: Understanding For Loops (15 minutes)

## Example Set A: Basic Pattern

```python
for friend in ['Joseph', 'Glenn', 'Sally']:
    print('Happy New Year:', friend)
print('Done!')
```

Questions:

1. What gets printed to the screen? Write down the exact output.
2. How many times does the indented line run?
3. What happens to the variable 'friend' during each run?

## Example Set B: Variations

```python
# Program 1
for letter in 'Hi!':
    print(letter)

# Program 2
for number in [1, 2, 3]:
    print('Count:', number)
```

Questions: 4. What's similar about how these two programs work? 5. What kinds of things can we put after the word 'in'? 6. In Program 1, what value does 'letter' have during each run?

## Example Set C: Loop Body

```python
# Program 3
for num in [1, 2]:
    print('Start')
    print(num)
    print('End')
print('All done')

# Program 4
for word in ['cat', 'dog']:
    answer = word + '!'
    print(answer)
```

Questions: 7. How many times does 'Start' get printed in Program 3? 8. What determines which lines are part of the loop? 9. What will Program 4 print? Be exact. 10. Based on all examples so far, describe in your own words what a for loop does.

# Explanation

<iframe width="100%" height="500" src="https://www.youtube.com/embed/JP7ITIXGpHk?start=234&end=1426" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Notes to capture:

- pros and cons of the first program that meows 3 times
- what will cause a loop to run forever?
- code for a working while loop
- sketch the flow of a while loop (flowchart or just arrows with code)
- two ways of incrementing (adding 1 to a variable)
- relationship between a for loop and a list
- syntax for a list
- when does a programmer use the variable "\_"

# For Loop Practice

## Part 1: Prediction Practice (5 minutes)

Students write the output for each program:

```python
# Program 1
for x in "wow":
    print("*")

# Program 2
for x in "wow":
    print(x)

# Program 3
for x in "wow":
    print(x + "!")
```

## Part 2: Code Writing (10 minutes)

Problems progress from guided to independent:

### Task 1: Complete the Code (with support)

```python
# Make this print:
# Go team!
# Go team!
# Go team!

for number in [1, 2, 3]:
    print(_________)  # Students fill in blank
```

### Task 2: Build from Template

```python
# Make this program print:
# hello a
# hello b
# hello c

for _____ in ['a', 'b', 'c']:
    ________________
```

### Task 3: Independent Writing

Write a for loop that prints:

```
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
```

## Part 3: Challenge (5 minutes)

For students who finish early:

```python
# Make this pattern:
# *
# **
# ***

# Hint: you can multiply strings!
# Example: "ha" * 3 gives "hahaha"
```

## Help Cards Available

Card 1: For Loop Template

```python
for variable_name in [value1, value2, value3]:
    print(variable_name)
```

Card 2: Common Patterns

```python
# Print same thing multiple times
for x in [1, 2, 3]:
    print("Hello")

# Print each value
for x in [1, 2, 3]:
    print(x)

# Print modified values
for x in [1, 2, 3]:
    print(x + 1)
```

# For Loop Wrap-up

## Quick Check (2 minutes)

Have students write and share with partner:
"A for loop is better than a while loop when..."

## Return to Opening Problem (1 minute)

Show original "headache" problem and its solution:

```python
# Original problem (messy):
count = 0
while count < 5:
    # Yikes... how do we print the right name?
    print("Hello", "???")
    count = count + 1

# Clean solution with for loop:
for name in ['Alice', 'Bob', 'Charlie', 'Diana', 'Eddie']:
    print("Hello", name)
```

## Exit Ticket (2 minutes)

Give students small paper slip with:

```python
# What will this print?
for letter in "bye":
    print(letter + letter)
```

Write:

1. The output
2. One question you still have about for loops
