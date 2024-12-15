# inventory.py
"""
Den här modulen innehåller funktioner för att hantera en ryggsäck (inventory).
Funktionerna gör det möjligt att lägga till saker, ta bort saker, byta plats på saker och visa innehållet i ryggsäcken.
"""


def pick(bag, item, position=None):
    """
    Adds an item to the bag either at the specified position or at the end.
    """
    if position is None:
        bag.append(item)
        print(f"{item} has been added at the end of the backpack.")
    else:
        try:
            position = int(position)
            if position < 0 or position > len(bag):
                print(f"Error: Position {position} is out of range.")
            else:
                bag.insert(position, item)
                print(f"{item} has been added at index {position}.")
        except ValueError:
            print("Error: Position must be a number.")
    return bag

def inventory(bag):
    """
    Displays the current contents of the backpack and its size.
  
    """
    print(f"Backpack has {len(bag)} item(s): {bag}")

def drop(bag, item):
    """
    Removes an item from the backpack.
  
    """
    try:
        bag.remove(item)
        print(f"{item} has been removed.")
    except ValueError:
        print(f"Error: {item} is not in the backpack.")
    return bag


def swap(bag, item1, item2):
    """
    Swap the positions of two items in the backpack.
    """
    if item1 in bag and item2 in bag:
        index1 = bag.index(item1)
        index2 = bag.index(item2)
        bag[index1], bag[index2] = bag[index2], bag[index1]
        print(f"{item1} and {item2} have swapped places.")
    else:
        # Use missing_items to clarify which items are missing
        missing_items = [item for item in [item1, item2] if item not in bag]
        print(f"Error: Missing items: {', '.join(missing_items)} in the bagpack")
      
    return bag
