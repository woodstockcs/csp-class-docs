---
title: Dictionaries
parent: Pete and Repeat
nav_order: 6
layout: default
---
# Dictionaries

## Sometimes lists aren't enough...
Players want the inventory to show when each item was found (sword='Monday 3pm', shield='Tuesday 2pm'). Using just lists, how would you match up items with their timestamps?

## Explanation
<iframe width="100%" height="500" src="https://www.youtube.com/embed/-7xg8pGcP6w?start=2735&end=3244" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Extending the Inventory System

```python
# Inventory system that tracks quantities of items using a dictionary
inventory = {}

def add_item(item, quantity):
    """
    Add items to inventory or increase quantity if item exists
    Returns True if successful
    """
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    return True

def remove_item(item, quantity):
    """
    Remove items from inventory
    Returns True if successful, False if item not in inventory or quantity too high
    """
    if item not in inventory:
        return False
    if inventory[item] < quantity:
        return False
    
    inventory[item] -= quantity
    # Remove item completely if quantity reaches 0
    if inventory[item] == 0:
        del inventory[item]
    return True

def has_item(item, quantity):
    """
    Check if an item is in inventory with at least the given quantity
    Returns True if item is in inventory with sufficient quantity
    """
    return item in inventory and inventory[item] >= quantity

def list_items():
    """
    Print all items currently in inventory with their quantities
    """
    if not inventory:
        print("Inventory is empty!")
        return
        
    print("\nCurrent inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def count_items():
    """
    Return the total number of individual items in inventory
    """
    return sum(inventory.values())

def run_tests():
    """
    Run tests on all inventory functions with detailed feedback
    """
    def run_test(name, actual, expected):
        """Helper function to run a single test"""
        passed = actual == expected
        print(f"{'✓' if passed else '✗'} {name}")
        if not passed:
            print(f"  Expected: {expected}")
            print(f"  Got: {actual}")
        return passed

    print("\n=== RUNNING INVENTORY TESTS ===")
    tests_passed = 0
    total_tests = 0

    # Clear inventory before tests
    inventory.clear()
    
    # Test adding items
    print("\nTesting add_item:")
    tests_passed += run_test("Add new notebook", add_item("notebook", 2), True)
    tests_passed += run_test("Add more notebooks", add_item("notebook", 3), True)
    tests_passed += run_test("Notebook quantity", inventory.get("notebook"), 5)
    total_tests += 3
    
    # Test checking for items
    print("\nTesting has_item:")
    tests_passed += run_test("Has 1 notebook", has_item("notebook", 1), True)
    tests_passed += run_test("Has 5 notebooks", has_item("notebook", 5), True)
    tests_passed += run_test("Has 6 notebooks", has_item("notebook", 6), False)
    tests_passed += run_test("Has pencil", has_item("pencil", 1), False)
    total_tests += 4
    
    # Test removing items
    print("\nTesting remove_item:")
    tests_passed += run_test("Remove 2 notebooks", remove_item("notebook", 2), True)
    tests_passed += run_test("Notebooks remaining", inventory.get("notebook"), 3)
    tests_passed += run_test("Remove too many", remove_item("notebook", 4), False)
    tests_passed += run_test("Remove nonexistent", remove_item("pencil", 1), False)
    total_tests += 4
    
    # Test counting
    print("\nTesting count_items:")
    tests_passed += run_test("Total item count", count_items(), 3)
    total_tests += 1

    # Print summary
    print(f"\nTests completed: {tests_passed}/{total_tests} passed")
    print("=" * 30)

def main():
    """
    Main game loop with menu interface
    """
    while True:
        print("\n=== INVENTORY MENU ===")
        print("1. Add items")
        print("2. Remove items")
        print("3. Check for items")
        print("4. List all items")
        print("5. Count total items")
        print("6. Run tests")
        print("7. Quit")
        
        choice = input("\nWhat would you like to do? ")
        
        if choice == "1":
            item = input("Enter item to add (e.g., notebook, pencil): ")
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive!")
                    continue
                
                if add_item(item, quantity):
                    print(f"{quantity} {item}(s) were added!")
                else:
                    print("Couldn't add items.")
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == "2":
            item = input("Enter item to remove: ")
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive!")
                    continue
                
                if remove_item(item, quantity):
                    print(f"{quantity} {item}(s) were removed!")
                else:
                    print("Couldn't remove items.")
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == "3":
            item = input("Enter item to check for: ")
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive!")
                    continue
                
                if has_item(item, quantity):
                    print(f"Yes, you have at least {quantity} {item}(s)!")
                else:
                    print(f"No, you don't have {quantity} {item}(s).")
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == "4":
            list_items()
            
        elif choice == "5":
            print(f"You have {count_items()} total items.")
            
        elif choice == "6":
            run_tests()
            
        elif choice == "7":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

## Code Reading Questions

### Easy
1. What does `inventory = {}` create at the start of the program? 

2. In `list_items()`, what gets printed if the inventory is empty?

3. If we call `add_item("pencil", 3)`, what will be stored in the inventory dictionary?

4. In the main menu, which option number is used to quit the program?

5. What symbol does the test function print when a test passes? What about when it fails?

### Medium
6. Look at this code in `has_item()`:
```python
return item in inventory and inventory[item] >= quantity
```
What are the TWO conditions that must both be true for this to return True?

7. In `remove_item()`, what are the TWO conditions that cause the function to return False?

8. Find where user input is converted to a number. What Python function is used for this conversion?

9. In the main menu, what happens if a user enters "8" as their choice?

10. What is the purpose of this line in `remove_item()`?
```python
if inventory[item] == 0:
    del inventory[item]
```

### Harder
11. Look at this code from `main()`:
```python
try:
    quantity = int(input("Enter quantity: "))
    if quantity <= 0:
        print("Quantity must be positive!")
        continue
```
What TWO things is this code checking for?

12. The `run_test()` function inside `run_tests()` takes three parameters: `name`, `actual`, and `expected`. What is the purpose of each one?

13. How does the `count_items()` function calculate the total number of all items in the inventory? What dictionary method does it use?

14. What is printed?
```python
add_item("notebook", 5)
print(remove_item("notebook", 3))
print(remove_item("notebook", 3))
```

15. What's different and similar between these two approaches to checking quantities:
```python
if item in inventory:
    if inventory[item] >= quantity:
        # do something
```
```python
if item in inventory and inventory[item] >= quantity:
    # do something
```

### Most Challenging
16. The program maintains a count of passed tests in `run_tests()`. Find all the places where `tests_passed` is modified. What is the purpose of the `+=` operator here?

17. When removing items, the code checks conditions in this order:
```python
if item not in inventory:
    return False
if inventory[item] < quantity:
    return False
```
 - Why is this order important? What could go wrong if we checked the quantity first?

18. In `run_tests()`, why do we need to call `inventory.clear()` at the start of the tests?

19. Look at how the test results are displayed:
```python
print(f"{'✓' if passed else '✗'} {name}")
```
- This is an f-string with a conditional expression. Explain how it decides which symbol to print.

20. Look at the code below. Some people think `Pencil` and `pencil` should be treated as the same item, and counted as 5 in the code below. What do you think: should they be handled as the same? How would you update the code to do this?
```python
add_item("Pencil", 3)
add_item("pencil", 2)
list_items()
# Shows:
# Pencil: 3
# pencil: 2
```

21. Look at this part of the `run_tests()` function:
```python
def run_test(name, actual, expected):
    """Helper function to run a single test"""
    passed = actual == expected
    print(f"{'✓' if passed else '✗'} {name}")
    if not passed:
        print(f"  Expected: {expected}")
        print(f"  Got: {actual}")
    return passed
```
What's unusual about this? Why is there a function defined inside another function? What do you think "Helper function" means?

22. Look at the text between triple quotes after each function definition:
```python
def add_item(item, quantity):
    """
    Add items to inventory or increase quantity if item exists
    Returns True if successful
    """
```
What do you think these triple-quoted strings are for? Why are they placed right after the function definition?
