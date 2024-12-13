---
title: Skill 1. Functions
parent: Python
nav_order: 1
layout: default
---
# On this page:
{: .no_toc }

1. TOC
{:toc}

# Lesson 1: Functions

## Lecture Notes on Functions

1. Grab a paper copy of the template for Lecture Notes on Functions (or print one from [here](https://docs.google.com/document/d/1jGGe0zvTKSy2NScz_apJhMdjNdMazeOgmOydYMoFoZM/edit)).
1. Complete the notes while you watch from 3:54 to 23:46 of this David Malan lecture on Functions (~20 min).

<iframe width="100%" height="500" src="https://www.youtube.com/embed/JP7ITIXGpHk?start=234&end=1426" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Practice Set on Functions

1. Write and run the program from the end of the lecture.
2. Make a custom mad-libs.
   - try multiple inputs
   - try something like `print("Hello " + name + "!")`

# Lesson 2: Variables

## Lecture Notes on Variables

1. Grab a paper copy of the template for Lecture Notes on Variables (or print one from [here](https://docs.google.com/document/d/1DxCjQCjXS60Hwf_VOeEspUnPQQFD9TD1_itjAaL2v7o/edit)).
1. Complete the notes while you watch the following THREE clips of David Malan talking about Variables (~21 min).

### Clip #1

25:00 to 29:35, which is 5 minutes about printing on one line

<iframe width="100%" height="500" src="https://www.youtube.com/embed/JP7ITIXGpHk?start=1500&end=1775" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Clip #2

1:03:05 to 1:10:17, which is 8 minutes about numbers

<iframe width="100%" height="500" src="https://www.youtube.com/embed/JP7ITIXGpHk?start=3785&end=4217" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Clip #3

1:26:13 to 1:33:28, which is 8 minutes about creating your own custom functions

<iframe width="100%" height="500" src="https://www.youtube.com/embed/JP7ITIXGpHk?start=5173&end=5608" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Practice Set on Variables

### Hello

If you are feeling:
{: .d-inline-block }

Less Comfy
{: .label .label-green }

1. Type `cd`. This takes you to your home directory, no matter where you are.
1. Type `ls` to confirm. You should see just the kitchen directory.
1. Make a new directory called `1-python`. (that's a ONE, not an L... that'll help later with sorts).
1. `cd` into that directory and type `code hello.py`.
1. Write a short python program that prints hello world. (Feel free to add a creative touch.)

---

### Add

If you are feeling:
{: .d-inline-block }

Less Comfy
{: .label .label-green }

1. Make sure you are in the directory called `1-python`.
1. Create a file called `add.py`
1. Write a python program that:
   - [ ] Asks the user for two numbers
   - [ ] Prints the result of adding those numbers together
<script src="https://asciinema.org/a/SIFEFvSpKEJXSP1PKjDiVHTJn.js" id="asciicast-SIFEFvSpKEJXSP1PKjDiVHTJn" async="true"></script>
---

### Hello 2

If you are feeling:
{: .d-inline-block }

Less Comfy
{: .label .label-green }

1. Make sure you are in the directory called `1-python`.
1. Create a file called `hello2.py`
1. Write a python program that:
   - [ ] Defines a custom function that prints "hello, " and the user's name
   - [ ] Asks the user for their name
   - [ ] Calls the custom function to greet the user

---

### What??

If you are feeling:
{: .d-inline-block }

Mixed
{: .label .label-yellow }

1. Make sure you are in the directory called `1-python`.
1. Create a file called `what.py`
1. Write a python program that:
   - [ ] Asks the user for a noun and verb
   - [ ] Puts them into a silly sentence using + concatenation, maybe something like:
     - "Yesterday, my [noun] suddenly [verb] underwater."
     - "The sleepy [noun] accidentally [verb] upside down."
   - [ ] Prints "What??"
   - [ ] Prints the same silly sentence again, but this time using print() with multiple arguments instead of the plus sign

---

### Custom Calculator

If you are feeling:
{: .d-inline-block }

More Comfy
{: .label .label-red }

In your `1-python` directory, create one or more custom calculator programs.

- Handle decimal inputs with `float()` instead of `int()`.
- Try implementing a complex formula from science or math or a sport or a game.
- Check out the `round()` function [here](https://www.w3schools.com/python/ref_func_round.asp).


# Lesson 3: String Functions

## Lecture Notes on String Functions

1. Grab a blank sheet of paper and take notes on the important elements.
1. Complete the notes while you watch from 41:03 to 53:36 of this David Malan lecture on Functions (~13 min).

<iframe width="100%" height="500" src="https://www.youtube.com/embed/JP7ITIXGpHk?start=2463&end=3216" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Practice Set on String Functions

### Hello 3

If you are feeling:
{: .d-inline-block }

Less Comfy
{: .label .label-green }

Write and run one of the programs shown in the lecture that uses `.split()` and `.title()`.

### Indoor Voice

If you are feeling:
{: .d-inline-block }

Mixed
{: .label .label-yellow }

Do the [Indoor Voice problem](https://cs50.harvard.edu/python/2022/psets/0/indoor/) from Harvard's CS50-P course, but you can skip the "How To Submit" part at the end.

### Making Faces

If you are feeling:
{: .d-inline-block }

More Comfy
{: .label .label-red }

Do the [Making Faces problem](https://cs50.harvard.edu/python/2022/psets/0/faces/) from Harvard's CS50-P course. See if you can do it via string functions (not *if* statements). Skip the "How To Submit" part at the end.


