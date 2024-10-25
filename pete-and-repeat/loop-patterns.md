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

# Part 4. Practice

## 4.1 Cookie Counter

You're helping at a bake sale. Create a program that:

- Takes a list of cookie sales per hour [12, 8, 15, 13, 7]
- Calculates and prints the total cookies sold
- Counts how many hours had sales above 10 cookies
- Finds the hour with the least sales

## 4.2 DNA Scanner

Scientists need help analyzing DNA sequences. Write a program that:

```python
dna = "AACTGCTA"
# Count how many times 'A' appears
# Build a new string with all 'A's replaced by 'T's
```

## 4.3 Password Strength

Create a password scoring system:

```python
password = "H3llo!World"
score = 0
# Add 1 point for each character
# Add 2 bonus points for each number
# Add 3 bonus points for each symbol (!@#$%^&*()?)
# Print the final score
```

## 4.4 Train Route Builder

**Question:** Use loops to build this train route display:

```
[Start]
[Start] --> Albany
[Start] --> Albany --> Boston
[Start] --> Albany --> Boston --> Chicago
[Start] --> Albany --> Boston --> Chicago --> Detroit
```

**Bonus Challenge:** Modify your code to also print the return journey:

```
Detroit --> Chicago --> Boston --> Albany --> [Start]
```
