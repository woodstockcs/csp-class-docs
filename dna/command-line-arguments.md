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

if (len(sys.argv) > 3):
    print("Hmm... I don't really want more than 3 arguments.")
    sys.exit()

print()
print("OK, here's what you told me:")
for word in sys.argv[1:]:
    print(word + " ")
```

Now run that program from the command line 4 times, like below.

{: .highlight}

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
> Make sure your name is on the walkthrough paper, drop it in the INBOX, then check the box in your sprint notes.

<br><br>

## Exercises

<!-- prettier-ignore-start -->

### hello.py
{: .d-inline-block }
Approaching
{: .label .label-green }

1. Copy/paste the code below into a new file called `hello.py`.
1. Update the code according to the comments.

```python
# Create a program that:
# - Takes a name as command line argument
# - Uses a Guard Clause to print a usage message and exit (if needed)
# - Prints "Hello, [name]!"
```

{: .note-title}

> Before continuing:
>
> Rename the sketch `Freezing` and save it.
>
> Then write that name in your sprint notes.

<br><br>

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
