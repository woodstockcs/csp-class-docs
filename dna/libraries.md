---
title: 2. Libraries
parent: DNA Sprint
nav_order: 3
layout: default
---

# Topic
Today's topic is **Libraries**.

All the purple boxes below indicate things to write on your [sprint notes](https://docs.google.com/document/d/1OYb_ZXyfsvn03kMQ8d-ZoNxDCCvYakIet19lYNmfJyk/edit?tab=t.0).

<br><br>

# Purpose

<table>
  <tr>
    <th>Learning:</th>
    <td style="width:100%">learn how to use functions from libraries</td>
  </tr>
  <tr>
    <th>DNA Project:</th>
    <td style="width:100%">use csv library to bring data in from files</td>
  </tr>
</table>

<br><br>

# Sandbox

```
(code to read)

(about lists?)
```
<br>

{: .note-title}

> Write in your sprint notes...
> review Qs.
> then a guess or two about that code. that we can talk about

<br><br>

# Walkthrough


1. Grab the [walkthrough paper](https://docs.google.com/document/d/1tYE56_PYmzqzeV2K0PW0Lw6qhjAlTiHEoL3dY_jp9ug/edit?usp=sharing) from the classroom.
1. Annotate the walkthrough paper while you watch [this video](https://youtu.be/EHi0RDZ31VA?start=7235&end=7426) (2:00:35 - 2:03:46).

{: .note-title}

> Before continuing:
>
> Check the box in your sprint notes to indicate that you annotated the paper.
>
> You might find this paper helpful in the exercises below.
>
> After that, hang on to this paper because you'll use it again on Assessment Day.

<br><br>

# Exercises

<!-- prettier-ignore-start -->

### dna.py
{: .d-inline-block }
2-Approaching
{: .label .label-green }

change up one of the exercises in claude

{: .highlight-title}

> Hint
>
> Try this on your own first, then have a look at the _STEP 1_ of the [sample solution code](https://docs.google.com/document/d/1uEKkKnHvat5I9iBBJ1sz58rK8TULenc6e44r36M6vcs/edit?tab=t.0) to check and fix your code.


{: .note-title}

> Write in your sprint notes...
>
> Why is it good for a Guard Clause to print a usage message?

<br><br>

### hello.py
{: .d-inline-block }
3-Proficient
{: .label .label-blue }

update the dna code. give instructions step by step. make sure you run it and get X.


```python
# DNA Exercise: hello.py
# - Takes a name as command line argument
# - Uses a Guard Clause to print a usage message and exit (if needed)
# - Prints "Hello, [name]!"

import sys

if len(sys._____)  ___  ___:
    print("Usage: python _____ _____")
    sys.______

print("Hello", _______)
```

{: .note-title}

> Write in your sprint notes...
>
> What happens if the user just runs `python hello.py`?

<br><br>



### repeat.py
{: .d-inline-block }
4-Distinguished
{: .label .label-red }

bigger claude

```python
# DNA Exercise: repeat.py
# - Accepts a word and number (e.g. "python repeat.py hello 3")
# - Prints the word that many times
# - Uses guard clauses for validation
# - Converts string number to integer safely

import sys

```

{: .note-title}

> Write in your sprint notes...
>
> What's a code snippet that is important to the functionality of your program?

<br><br>

### calc.py
{: .d-inline-block }
5,000 Fake Bonus Points
{: .label .label-red }

one more claude

```python
# DNA Exercise: calc.py
# - Accepts 3 args: two numbers and an operator (+,-,x,/)
# - Uses guard clauses to check that the user provided
#   a number, a valid operator, and another number
# - Prints "Usage: python calculator.py num1 op num2" if invalid
# - Prints the expression and its result
# - Handles divide-by-zero gracefully

```

{: .highlight-title}

> Note
>
> For this exercise, accept `x` for multipy, not `*`. The reason? The shell, where you type the command-line arguments, treats `*` as a special character. If you type `*` as a command-line argument, the shell will replace your `*` with a list of all the filenames in the current directory and send that to python. That's definitely not what we want! So ask the user to use `x` if they want to multiply.


{: .note-title}

> Write in your sprint notes...
>
> How many times does your program contain the keyword `if`?

<br><br>

<!-- prettier-ignore-end -->
