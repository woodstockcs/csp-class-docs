---
title: Command-Line Arguments
parent: DNA
nav_order: 2
layout: default
---

# Command-Line Arguments

## Purpose

<table>
  <tr>
    <th>Learning:</th>
    <td>use command-line arguments with error handling</td>
  </tr>
  <tr>
    <th>DNA Project:</th>
    <td>accept two file names as command-line arguments</td>
  </tr>
</table>

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

## Walkthrough

Watch [this video](https://youtu.be/EHi0RDZ31VA?start=7235&end=7426) (2:00:35 - 2:03:46).

And take notes on [this doc](https://docs.google.com/document/d/1tYE56_PYmzqzeV2K0PW0Lw6qhjAlTiHEoL3dY_jp9ug/edit?usp=sharing).

## Exercises

<!-- prettier-ignore-start -->

### 1. hello.py
{: .d-inline-block }
Approaching
{: .label .label-green }

```python
# Create a program that:
# - Takes a name as command line argument
# - Uses a Guard Clause to print a usage message and exit (if needed)
# - Prints "Hello, [name]!"
```

### 2. dna.py
{: .d-inline-block }
Approaching
{: .label .label-green }

```python
# Open the dna.py file provided in the distribution code.
# - Under "Check for command-line usage", write a Guard Clause
# - If there are not 3 arguments, print a usage message and exit
# - Print a message indicating the names of the two input files that will be used.
```

### 3. repeat.py
{: .d-inline-block }
Proficient
{: .label .label-blue }

```python
# Create a program that:
# - Accept a word and number (e.g. "python repeat.py hello 3")
# - Print the word that many times
# - Use guard clauses for validation
# - Convert string number to integer safely
```

### 4. calculator.py
{: .d-inline-block }
Distinguished
{: .label .label-red }

```python
# Create a program that:
# - Accept 3 args: two numbers and an operator (+,-,*,/)
# - Print "Usage: python calculator.py num1 op num2" if invalid
# - Use guard clauses for validation
# - Handle divide-by-zero gracefully
```
<!-- prettier-ignore-end -->
