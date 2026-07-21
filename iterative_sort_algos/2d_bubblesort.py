def bubblesort(data, key_index):
    num_rows = len(data)
    for pass_num in range(num_rows - 1):
        for row_index in range(num_rows - pass_num - 1):
            current_key = data[row_index][key_index]
            next_key = data[row_index + 1][key_index]
            if current_key > next_key:
                # Swap the entire rows
                data[row_index], data[row_index + 1] = data[row_index + 1], data[row_index]
                return data

# Example Data: [ Item, Price, Stock ]
store_items = [
    ["Bread", 3.50, 150],
    ["Milk", 1.80, 200],
    ["Eggs", 4.25, 90],
    ["Cheese", 5.00, 120]
]

# Sorting by Price (Column Index 1)
PRICE_INDEX = 1

print("Original Data:")
for row in store_items:
    print(row)

sorted_data = bubblesort(store_items, PRICE_INDEX)

print("\nSorted by Price (Column 1):")
for row in sorted_data:
    print(row)