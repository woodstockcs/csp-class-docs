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
