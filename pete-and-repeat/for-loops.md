---
title: For Loops
parent: Pete and Repeat
nav_order: 2
layout: default
---

# For Loops

# Part 1 Warmup (5 minutes)

## 1.1

```python
count = 0
while count < 3:
    print("Hello")
    count = count + 1
```

**Question:** How many times will this code print "Hello"?

## 1.2

```python
friend = "Alice"
print("Hello", friend)
friend = "Bob"
print("Hello", friend)
```

**Question:** What will this code print?

## 1.3

```python
# We want to say hello to 5 friends:
# Alice, Bob, Charlie, Diana, and Eddie

count = 0
while count < 5:
    # Yikes... how do we print the right name?
    print("Hello", "???")
    count = count + 1
```

**Question:** Using only what we know about while loops and variables, how could we solve this? What makes it awkward or difficult?

# Part 2. Predictions (15 minutes)

## 2.1

```python
for friend in ['Joseph', 'Glenn', 'Sally']:
    print('Happy New Year:', friend)
print('Done!')
```

**Questions:**

- a. What gets printed to the screen? Write down the exact output.
- b. How many times does the indented line run?
- c. What happens to the variable 'friend' during each run?

## 2.2

```python
# Program 1
for letter in 'Hi!':
    print(letter)
```

```python
# Program 2
for number in [1, 2, 3]:
    print('Count:', number)
```

**Questions:**

- a. What's similar about how these two programs work?
- b. What kinds of things can we put after the word 'in'?
- c. In Program 1, what value does 'letter' have during each run?

## 2.3

```python
# Program 3
for num in [1, 2]:
    print('Start')
    print(num)
    print('End')
print('All done')
```

```python
# Program 4
for word in ['cat', 'dog']:
    answer = word + '!'
    print(answer)
```

**Questions:**

- a. How many times does 'Start' get printed in Program 3?
- b. What determines which lines are part of the loop?
- c. What will Program 4 print? Be exact.

# Part 3. Lecture Notes (15 minutes)

<iframe width="100%" height="500" src="https://www.youtube.com/embed/-7xg8pGcP6w?start=980&end=1395" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# Part 4. Practice

## 4.1

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

**Question:** What is the output of these 3 programs?

## 4.2

```python
# template
for _____ in ['a', 'b', 'c']:
    ________________
```

**Question:** Adapt the template code (just above) to print this:

```python
hello a
hello b
hello c
```

## 4.3

**Question:** Write a for loop that prints:

```
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
```

## 4.4

**Question:** Use a for loop to make python print this pattern:

(Hint: you can multiply strings! Example: `"ha" * 3` gives `"hahaha"`)

```python
*
**
***
****
```

**Bonus Challenge:** Use a for loop to print one of these patterns:

```python
   *
  **
 ***
****
```

```python
  *
 ***
*****
 ***
  *
```
