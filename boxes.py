import math

# ask user the number of manufactured items
num_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

boxes = math.ceil(num_items / items_per_box)

print(f"For {num_items} items, packing {items_per_box} items in each box, you will need {boxes} boxes.")

# ask the number of items that the user will pack per box