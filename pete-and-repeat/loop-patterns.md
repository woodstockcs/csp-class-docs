---
title: Loop Patterns
parent: Pete and Repeat
nav_order: 3
layout: default
---

# Loop Patterns

# Part 1 Warmup (5 minutes)

## 1.1

```python
for letter in "STOP":
    print(letter)
    print("-")
```

**Question:** How many total lines will this code print?

## 1.2

```python
total_score = 0
for round_score in [10, 25, 5]:
    print("You scored:", round_score)
print("Your total score is", total_score)
```

**Question:** What's wrong with this program?

## 1.3

```python
word = ""
for letter in "CAKE":
    word = letter + "."
print(word)
```

**Question:** I want this code to print C.A.K.E. but it doesn't. What does it print? Any thoughts on how to fix it?

# Part 2. Predictions (15 minutes)

## 2.1 Score Keeper

```python
total = 0
for points in [15, 8, 12, 9]:
    total = total + points
    print("Running total:", total)
print("Final score:", total)
```

**Questions:**

- a. What gets printed each time through the loop?
- b. What is happening to the 'total' variable?
- c. Is this different from just setting total = 15 + 8 + 12 + 9?

## 2.2 Weather Tracker

```python
# Program 1
temps = [72, 75, 71, 73, 74]
above_73 = 0
for temp in temps:
    if temp > 73:
        above_73 = above_73 + 1
print(above_73, "days were above 73°")
```

```python
# Program 2
temps = [72, 75, 71, 73, 74]
highest = 0
for temp in temps:
    if temp > highest:
        highest = temp
print("Highest temperature was", highest)
```

**Questions:**

- a. What is each program calculating?
- b. What's similar about how they use their variables (above_73 and highest)?
- c. When does each program update a variable?

## 2.3 Word Builder

```python
# Program 1
message = ""
for word in ["Time", "to", "code"]:
    message = message + word + " "
print(message)
```

```python
# Program 2
exclamations = ""
for count in [1, 2, 3]:
    exclamations = exclamations + "!"
print("Wow" + exclamations)
```

**Questions:**

- a. What will each program print? Be exact.
- b. How are the programs similar in how they build up their strings?
- c. Why do we need to add the space " " in Program 1?

# Part 3. Explanation (15 minutes)
Check out the patterns [here](https://www.online-python.com/AFv5bq7Spy).

# Part 4. Practice

## 4.1 Beginning: Step Counter
```python
steps = [1089, 7392, 5324, 8543]
# Calculate total steps taken
```
Hint: This uses the running total pattern. Start with total = 0.

## 4.2 Approaching: Score Tracker
```python
scores = [88, 92, 85, 95, 88]
# Count how many scores are at least 90
# Print the number of A grades
```
Hint: Use a counter starting at 0, add 1 each time you find a score >= 90.
## 4.3 Proficient: Word Formatter
```python
word = "PYTHON"
# Create a string that puts dots between each letter
# Should print: P.Y.T.H.O.N
```
Hint: Build the string one character at a time. Think about when to add the dots.
## 4.4 Distinguished: Shopping Cart
```python
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
# Count how many of each item is in the cart
# Print: "apple: 3, banana: 2, orange: 1"
```
Hint: You'll need to combine patterns. Consider keeping track of unique items as you find them.

## Optional Bonus Challenge

**Question:** Use loops to build this train route display:

```
[Start]
[Start] --> Albany
[Start] --> Albany --> Boston
[Start] --> Albany --> Boston --> Chicago
[Start] --> Albany --> Boston --> Chicago --> Detroit
```

**Bonus Bonus Challenge:** Modify your code to also print the return journey:

```
Detroit --> Chicago --> Boston --> Albany --> [Start]
```
