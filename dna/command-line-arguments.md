---
title: Command-Line Arguments
parent: DNA
nav_order: 2
layout: default
---

# Topic
Today's topic is **Command-Line Arguments**.

<br><br>

# Purpose

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

<br><br>

# Sandbox

Paste this code into a new file called `arguments.py`.
```python
import sys

print("You gave me", len(sys.argv), "command-line arguments.")
print("The first one is:", sys.argv[0])
print("The second one is:", sys.argv[1])

if len(sys.argv) > 3:
    print("Hmm... I don't really want more than 3 arguments.")
    sys.exit()

print()
print("OK, here's what you told me:")
for word in sys.argv[1:]:
    print(word + " ")
```

Now run that program from the command line 4 times, like below.

{: .highlight-title}

> Hint
>
> After each run, save some typing by pressing the `up-arrow` key and then just adding one word.

```
#   python arguments.py
#   python arguments.py Computer
#   python arguments.py Computer Science
#   python arguments.py Computer Science Rocks
```

{: .note-title}

> Write in your sprint notes...
>
> three things you notice or wonder about `arguments.py` and its output.

<br><br>

## Walkthrough


1. Grab the [walkthrough paper](https://docs.google.com/document/d/1tYE56_PYmzqzeV2K0PW0Lw6qhjAlTiHEoL3dY_jp9ug/edit?usp=sharing) from the classroom.
1. Annotate the walkthrough paper while you watch [this video](https://youtu.be/EHi0RDZ31VA?start=7235&end=7426) (2:00:35 - 2:03:46).

{: .note-title}

> Before continuing:
>
> Check the box in your sprint notes to indicate that you finished this task.
>
> You might find this paper helpful in the exercises below.
>
> After that, hang on to this paper because you'll use it again on Assessment Day.

<br><br>

## Exercises

<!-- prettier-ignore-start -->

### hello.py
{: .d-inline-block }
2-Approaching
{: .label .label-green }

1. Copy/paste the code below into a new file called `hello.py`.
1. Update the code according to the comments.

```python
# DNA Exercise: hello.py
# Update the code below so it:
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

> Exercise Note
>
> What happens if the user just runs `python hello.py`?

<br><br>

### dna.py
{: .d-inline-block }
3-Proficient
{: .label .label-blue }

1. Open the dna.py file provided in the distribution code.
1. Under "# Check for command-line usage", write a Guard Clause that requires 3 arguments to continue. Meaning: If there are **not** 3 arguments, print a usage message and exit
1. After passing the Guard Clause, show a user-friendly log message indicating the names of the two input files that will be used.

{: .note-title}

> Exercise Note
>
> Why is it good for a Guard Clause to print a usage message?

<br><br>

### repeat.py
{: .d-inline-block }
4-Distinguished
{: .label .label-red }

1. Copy/paste the code below into a new file called `repeat.py`.
1. Write code according to the comments.

```python
# DNA Exercise: repeat.py
# - Accepts a word and number (e.g. "python repeat.py hello 3")
# - Prints the word that many times
# - Uses guard clauses for validation
# - Converts string number to integer safely

import sys

```

{: .note-title}

> Exercise Note
>
> What's a code snippet that is important to the functionality of your program?

<br><br>

### calc.py
{: .d-inline-block }
5,000 Fake Bonus Points
{: .label .label-red }

1. Copy/paste the code below into a new file called `calc.py`.
1. Write code according to the comments.

```python
# DNA Exercise: calc.py
# - Accepts 3 args: two numbers and an operator (+,-,*,/)
# - Uses guard clauses to check that the user provided
#   a number, a valid operator, and another number
# - Prints "Usage: python calculator.py num1 op num2" if invalid
# - Prints the expression and its result
# - Handles divide-by-zero gracefully

```

{: .note-title}

> Exercise Note
>
> How many times does your program contain the keyword `if`?

<br><br>

<!-- prettier-ignore-end -->
