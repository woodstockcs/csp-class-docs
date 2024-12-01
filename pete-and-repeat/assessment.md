---
title: Assessment
parent: Pete and Repeat
nav_order: 7
layout: default
---

<br>

{: .warning-title }

> Just So You Know
>
> This page is currently a work-in-progress.

<br>

# Assessment

## Learning Goals

#### While Loops

- Explain how while loops work, including the risk of infinite loops
- Use a while loop with a counter variable to repeat code a specific number of times
- Increment variables using both `x = x + 1` and `x += 1` syntax
- Write for loops that iterate over lists and ranges
- Use `range()` to generate lists of numbers for loops (single-argument version only)
- Convert between while loops and for loops to solve the same problem

#### Lists

- Create lists using square bracket syntax [item1, item2, ...]
- Access list elements using index notation (both positive and negative indices)
- Modify list elements using index assignment
- Check if an item exists in a list using the in operator
- Get the length of a list using len()
- Use basic list methods like .append() and .remove()

#### Patterns

- Implement the Running Sum Pattern to calculate totals
  - Initialize an accumulator to 0
  - Add each item from a sequence to the accumulator
- Use the Running Product Pattern for multiplication sequences
  - Initialize an accumulator to 1
  - Multiply each item into the accumulator
- Apply the Counter Pattern to count occurrences
  - Initialize a counter to 0
  - Increment counter when specific conditions are met
- Implement the String Building Pattern
  - Initialize an empty string
  - Concatenate new strings with spacing/formatting
- Use the Running Maximum Pattern to find highest values
  - Initialize with first value
  - Update when finding larger values
- Apply the Filtered Accumulation Pattern
  - Accumulate values only when they meet certain conditions
- Recognize which pattern to use for different problems

# Review Game

https://docs.google.com/document/d/1fgm_EDuWVHj1fppYCG4nL9UpzpN_-p-j4d0GOdO90gc/edit?tab=t.0

# Loops Quiz

Based on Khan (LINK TO QUIZZES)

and (LINK TO While Loops + For Loops pages)

# Lists Quiz

Based on Khan (LINK TO QUIZZES)

and (LINK TO Lists Intro page)

# Practice Performance Task

Based on (LINK TO Lists Patterns page)

# Data Explorer Project

In this project, you'll analyze real-world data using loop patterns we've learned. You'll pick a dataset you're interested in and use Python to answer questions about it.

## Setup: Loading Your Data

First, pick one of these datasets (provided as CSV files):

1. `movies.csv`: Top movies from 2000-2023 with ratings, budget, and box office earnings
2. `weather.csv`: Daily temperature, rainfall, and wind speeds for the past year
3. `video_games.csv`: Popular games with release dates, ratings, and player counts
4. `sports.csv`: Professional athlete statistics across different sports

Here's the code to load any of these files into lists:

```python
def load_data(filename):
    """Load data from CSV file into lists"""
    with open(filename) as f:
        # Skip header row
        next(f)

        # Create empty lists for each column
        col1, col2, col3, col4 = [], [], [], []

        # Read each line and split into columns
        for line in f:
            data = line.strip().split(',')
            col1.append(data[0])
            col2.append(float(data[1]))
            col3.append(float(data[2]))
            col4.append(float(data[3]))

    return col1, col2, col3, col4

# Example loading movie data:
titles, ratings, budgets, earnings = load_data('movies.csv')

# Example loading weather data:
dates, temps, rainfall, wind = load_data('weather.csv')

# Example loading game data:
games, ratings, players, hours = load_data('video_games.csv')

# Example loading sports data:
athletes, points, assists, rebounds = load_data('sports.csv')
```

## Project Levels

### Level 1: Beginning - Basic Sum/Average

At this level, you'll calculate a simple total or average using the Running Sum Pattern.

Example tasks:

- Calculate total rainfall for the year
- Find average movie rating
- Calculate total player hours across all games
- Find average points per athlete

Sample code to adapt:

```python
# Calculate average movie rating
total_rating = 0
for rating in ratings:
    total_rating = total_rating + rating
average_rating = total_rating / len(ratings)
print(f"Average rating: {average_rating:.1f}")
```

### Level 2: Approaching - Counting with Conditions

At this level, you'll count items that meet specific criteria using the Counter Pattern.

Example tasks:

- Count rainy days (rainfall > 0.1 inches)
- Count highly rated movies (rating > 8.0)
- Count popular games (players > 1 million)
- Count high-scoring games (points > 30)

Sample code to adapt:

```python
# Count highly rated movies
great_movies = 0
for i in range(len(titles)):
    if ratings[i] > 8.0:
        great_movies += 1
        print(f"Great movie: {titles[i]} ({ratings[i]})")
print(f"\nFound {great_movies} great movies!")
```

### Level 3: Proficient - Finding Extremes

At this level, you'll find maximum/minimum values and their associated items using the Running Maximum Pattern.

Example tasks:

- Find the hottest day and its temperature
- Find the most profitable movie and its earnings
- Find the most-played game and its player count
- Find the highest-scoring athlete and their score

Sample code to adapt:

```python
# Find most profitable movie
max_profit = earnings[0] - budgets[0]
max_profit_title = titles[0]

for i in range(len(titles)):
    profit = earnings[i] - budgets[i]
    if profit > max_profit:
        max_profit = profit
        max_profit_title = titles[i]

print(f"Most profitable movie: {max_profit_title}")
print(f"Profit: ${max_profit:,.2f}")
```

### Level 4: Distinguished - Advanced Analysis

At this level, you'll combine multiple patterns to perform more complex analysis.

Example tasks:

- Find the month with the highest average temperature
- Calculate the average profit for movies in each rating category
- Compare weekday vs weekend player counts for games
- Find the athlete with the best points-to-assists ratio

Sample code to adapt:

```python
# Analyze average profit by rating category
# First, create categories
low_rated = []
med_rated = []
high_rated = []

# Categorize movies
for i in range(len(titles)):
    profit = earnings[i] - budgets[i]
    if ratings[i] < 6.0:
        low_rated.append(profit)
    elif ratings[i] < 8.0:
        med_rated.append(profit)
    else:
        high_rated.append(profit)

# Calculate averages
def get_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

print("Average profit by rating category:")
print(f"Low rated (< 6.0): ${get_average(low_rated):,.2f}")
print(f"Medium rated: ${get_average(med_rated):,.2f}")
print(f"High rated (8.0+): ${get_average(high_rated):,.2f}")
```

## Requirements for All Levels:

1. Choose a dataset you're interested in
2. Write a clear question you want to answer
3. Use appropriate loop patterns to analyze the data
4. Print results in a clear, readable format
5. Add comments explaining your code
6. Test with different parts of the dataset

## Pro Tips:

- Start simple! Get basic analysis working before adding complexity
- Print intermediate results to check your logic
- Use descriptive variable names that match your data
- Remember to handle edge cases (empty lists, missing data)
- Consider using functions to organize your code

Need help? Here are some good questions to ask:

1. What pattern(s) will help me solve this?
2. What variables do I need to track?
3. What conditions am I checking for?
4. How will I know if my answer is reasonable?
