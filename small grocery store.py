fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Potato", "Tomato"]
beverages = ["Juice", "Water", "Soda"]

fruits.append("Mango")

vegetables.insert(1, "Cucumber")

beverages.pop()

inventory = [fruits, vegetables, beverages]

print("First two fruits:", fruits[:2])

print("Last vegetable:", vegetables[-1])

fruit_lengths = [len(fruit) for fruit in fruits]
print("Lengths of fruit names:", fruit_lengths)

print("Is Water in beverages?", "Water" in beverages)

first_items_tuple = (fruits[0], vegetables[0], beverages[0])
print("Tuple of first items:", first_items_tuple)

print("Inventory:", inventory)
