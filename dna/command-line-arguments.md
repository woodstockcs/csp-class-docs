---
title: Command-Line Arguments
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

## Explanation
Watch [this video](https://youtu.be/EHi0RDZ31VA?start=7235&end=7426) (2:00:35 - 2:03:46).

And take notes on [this doc](https://docs.google.com/document/d/1tYE56_PYmzqzeV2K0PW0Lw6qhjAlTiHEoL3dY_jp9ug/edit?usp=sharing).

## Practice

### dna/hello.py
```python
# Create a program that:
# - Takes a name as command line argument
# - Prints "Hello, [name]!" if a name is provided
# - Prints "Hello, world!" if no name is provided
```

### dna/repeat.py
```python
# Create a program that:
# - Accept a word and number (e.g. "python repeat.py hello 3")
# - Print the word that many times
# - Use guard clauses for validation
# - Convert string number to integer safely
```

### dna/calculator.py
```python
# Create a program that:
# - Accept 3 args: two numbers and an operator (+,-,*,/)
# - Print "Usage: python calculator.py num1 op num2" if invalid
# - Use guard clauses for validation
# - Handle divide-by-zero gracefully
```
