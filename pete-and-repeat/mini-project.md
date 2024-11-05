---
title: Mini-Project
parent: Pete and Repeat
nav_order: 5
layout: default
---

# Inventory System Mini-Project (30-45 minutes)
In this project, you'll build a simple inventory system like those found in games. The code includes a menu interface and testing system - you just need to implement the core functions! Next class, you'll review your code with a classmate.

## Helpful Python list commands:

```python
my_list.append(item)    # Adds item to end
my_list.remove(item)    # Removes first occurrence
item in my_list         # Checks if item exists
len(my_list)           # Gets number of items
```

## Your Tasks:
- Study the add_item() function - it's your example
- Implement the remaining functions
- Update the menu code to let the study run those functions
- Use run_tests() to check your work
- Try out your functions using the menu!

## Need help getting started?
- The add_item() function shows you how to modify the inventory list
- Remember that you can use in to check if something is in a list
- Use a for loop to print each item in list_items()

## Test your functions with different cases:
- Adding various items
- Removing items that exist and don't exist
- Checking for items that exist and don't exist
- Listing empty and non-empty inventories
- Counting items when inventory has different numbers of items

## Starter code
Copy this starter code into a new file:

```python
# List to store the player's items
inventory = []

def add_item(item):
    """
    Add an item to inventory
    Returns True if successful
    """
    # Here's one function implemented as an example:
    inventory.append(item)
    return True

def remove_item(item):
    """
    Remove an item from inventory
    Returns True if successful, False if item not in inventory
    """
    # TODO: Write this function
    return False

def has_item(item):
    """
    Check if an item is in inventory
    Returns True if item is in inventory, False otherwise
    """
    # TODO: Write this function
    return False

def list_items():
    """
    Print all items currently in inventory
    """
    # TODO: Write this function
    pass

def count_items():
    """
    Return the total number of items in inventory
    """
    # TODO: Write this function
    return 0

def run_tests():
    """
    Run tests on all inventory functions
    """
    print("\n=== TESTING INVENTORY SYSTEM ===")
    
    print("\nTesting add_item:")
    print(add_item("sword"))  # Should print: True
    
    print("\nTesting has_item:")
    print(has_item("sword"))  # Should print: True
    print(has_item("shield")) # Should print: False
    
    print("\nTesting list_items:")
    list_items()  # Should print the inventory
    
    print("\nTesting count_items:")
    print(count_items())  # Should print: 1
    
    print("\nTesting remove_item:")
    print(remove_item("sword"))  # Should print: True
    print(remove_item("shield")) # Should print: False
    
    print("\n=== TESTS COMPLETE ===")

def main():
    """
    Main game loop with menu interface
    """
    while True:
        print("\n=== INVENTORY MENU ===")
        print("1. Add item")
        print("2. Remove item")
        print("3. Check for item")
        print("4. List all items")
        print("5. Count items")
        print("6. Run tests")
        print("7. Quit")
        
        choice = input("\nWhat would you like to do? ")
        
        if choice == "1":
            item = input("Enter item to add: ")
            if add_item(item):
                print(f"{item} was added!")
            else:
                print("Couldn't add item.")
                
        elif choice == "2":
            item = input("Enter item to remove: ")
            
        elif choice == "6":
            run_tests()

            
        else:
            print("Invalid choice. Please try again.")

main()
```

# Code Review Checklist
Reviewer Name: _________________
Code Author: _________________

## 1. Built-in Tests (Option 6)
When you run the tests, you should see:
- [ ] add_item("sword") returns True
- [ ] has_item("sword") returns True
- [ ] has_item("shield") returns False
- [ ] list_items() shows only "sword"
- [ ] count_items() returns 1
- [ ] remove_item("sword") returns True
- [ ] remove_item("shield") returns False

## 2. Try These Manual Tests
Run through this exact sequence:

1. Pack your camping gear:
   - [ ] Add "tent"
   - [ ] Add "flashlight"
   - [ ] Add "matches"
   - [ ] List items (should show all 3)

2. Get ready for rain:
   - [ ] Add "umbrella" 
   - [ ] Check if you have "raincoat" (should say no)
   - [ ] Count items (should show 4)

3. Use some items:
   - [ ] Remove "matches" (used at campfire)
   - [ ] Remove "umbrella" (left in car)
   - [ ] List items (should show remaining 2)

4. Pack snacks:
   - [ ] Add "granola"
   - [ ] Add "granola"
   - [ ] Add "granola"
   - [ ] Count items (should show 5)
   - [ ] Remove "granola" (should remove one)
   - [ ] List items (should show 4 items, 2 granolas)

5. Try weird stuff:
   - [ ] Add "trail mix 2.0" (item with spaces/symbols)
   - [ ] Add "" (empty string)
   - [ ] Remove "NOT IN BAG" (non-existent item)
   - [ ] Check for "TENT" (case different from "tent")

## 3. Code Review
Look at their actual code:

### Function Implementation
For each function, mark if it's Complete, Partial, or Missing
- remove_item(): _____ 
- has_item(): _____
- list_items(): _____
- count_items(): _____

### Menu Implementation
Make sure these menu options work:
 - [ ] Option 3 (Check for item) - prints "Yes, you have {item}!" or "No, you don't have {item}."
 - [ ] Option 4 (List all items) - shows current inventory
 - [ ] Option 5 (Count items) - prints "You have {number} items."
 - [ ] Option 7 (Quit) - exits program, maybe with a goodbye message, and returns you to the terminal prompt $
 
### Code Quality
- Variable names make sense? _____
- Functions are easy to read? _____
- Code looks well-organized? _____
- Any clever solutions? _____

## Summary
A strength of this code is:


An improvement could be:


Remember: Be specific in your feedback!
