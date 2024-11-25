---
title: Libraries
parent: DNA
nav_order: 2
layout: default
---

## Sandbox
```python
# Try running this as:
#   python program.py
#   python program.py David
#   python program.py Hello World

from sys import argv
print("Number of arguments:", len(argv))
print("Arguments are:", argv)
print("The first one is:", argv[0])

```

## Notes
Watch [this video](https://youtu.be/EHi0RDZ31VA?si=T0z9_GFoLex5bZ7g&t=7185).

- What is argv and which library contains it?
- How do you count command line arguments in Python?

- Draw a diagram showing what argv contains when you run:
```python
python greet.py David
```

- Two ways to import from sys:

- Steps to use a new library:

## Practice

### Hello Argument
```python
# Create a program that:
# 1. Takes a name as command line argument
# 2. Prints "Hello, [name]!" if a name is provided
# 3. Prints "Hello, world!" if no name is provided
```

### Hello Cowsay
```python
# Create a program that:
# 1. Uses the cowsay library
# 2. Asks the user their name using input()
# 3. Makes the cow say "Nice to meet you, [name]!"
```

### QR
```python
# Create a program that:
# 1. Takes a URL as command line argument
# 2. Generates a QR code for that URL
# 3. Saves it as "website.png"
# 4. Handles errors appropriately
```
