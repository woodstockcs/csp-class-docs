<!--
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

Create a file called `deck.py` and paste this code:

```python
import random

# A mini card game setup
cards = ["Jack", "Queen", "King"]
print("Original deck:", cards)

# Shuffle the cards
random.shuffle(cards)
print("After shuffle:", cards)

# Draw a random card
chosen = random.choice(cards)
print("You drew:", chosen)
```

<br>
Try these experiments:

1. Run the program 10 times. Keep track of how many times you draw each card.
1. Add two more cards to the list (like "Ace" and "10").
1. Instead of drawing one card, draw two cards (use random.choice() twice).
1. Create a new list with numbers 1-6 (like a die) and use random.choice() on that instead.

{: .note-title}

> Write in your sprint notes...
> 
> something else you might use `random` for

<br><br>

# Walkthrough


1. Grab a blank paper and take notes while you watch [this video](https://www.youtube.com/watch?v=MztLZWibctI) (0:00:00 - 0:17:16).

{: .note-title}

> Before continuing:
>
> Check the box in your sprint notes to indicate that you watched the video and took notes.
>
> You might find your notes helpful in the exercises below.
>
> After that, hang on to your notes because you'll use them again on Assessment Day.

<br><br>

# Exercises


<!-- prettier-ignore-start -->

### coin_flipper.py
{: .d-inline-block }
2-Approaching
{: .label .label-green }

Create a program that:
- Takes a number as command line argument
- Flips a coin that many times
- Prints the percentage of heads vs tails

{: .note-title}

> Write in your sprint notes...
>
> the file name of your completed exercise.

<br><br>

### dice_game.py
{: .d-inline-block }
3-Proficient
{: .label .label-blue }
Create a dice game that:
- Rolls two dice
- Lets the user guess if the sum will be over/under 7
- Keeps track of wins/losses

```

{: .note-title}

> Write in your sprint notes...
>
> the file name of your completed exercise.

<br><br>



### food_fight.py
{: .d-inline-block }
4-Distinguished
{: .label .label-red }

Create a program that simulates silly food battles:
- Reads foods.csv 
- Picks two random foods to battle
- Uses just one stat (messiness) to determine winner
- Prints fun battle messages

Here's foods.csv:
```
food,messiness
spaghetti,8
jello,6
banana,4
pizza,7
taco,9
sandwich,3
pudding,5
```

Sample Solution:
```python
import random
import csv

# Read the foods
with open("foods.csv") as f:
    foods = list(csv.DictReader(f))

# Keep battling until user quits
while True:
    # Pick two random foods
    food1, food2 = random.sample(foods, 2)
    
    print(f"\n🥊 FOOD FIGHT! 🥊")
    print(f"{food1['food']} vs {food2['food']}")
    
    # Add some randomness to the messiness
    power1 = int(food1['messiness']) + random.randint(1,3)
    power2 = int(food2['messiness']) + random.randint(1,3)
    
    # Determine winner
    if power1 > power2:
        print(f"{food1['food']} wins by making a bigger mess!")
    else:
        print(f"{food2['food']} wins by making a bigger mess!")
    
    # Play again?
    again = input("\nAnother battle? (y/n) ")
    if again.lower() != 'y':
        break
  ```
{: .note-title}

> Write in your sprint notes...
>
> the file name of your completed exercise.

<br><br>


<!-- prettier-ignore-end -->
