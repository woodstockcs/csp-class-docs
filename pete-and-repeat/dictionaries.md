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

## Reading Questions
