def insertion_sort(data):
    for i in range(1, len(data)):
        
        current_item = data[i]
        j = i - 1
        
        while j >= 0 and current_item < data[j]:
            data[j + 1] = data[j]
            j -= 1
        
        data[j + 1] = current_item
        
    return data

# Example Use Case:
unsorted_list = [7, 2, 4, 1, 5, 3]

print(f"Original list: {unsorted_list}")

sorted_list = insertion_sort(unsorted_list)

print(f"Sorted list: {sorted_list}")


def recursive_insertion_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    # Recursively sort everything except the last element
    sorted_prefix = recursive_insertion_sort(arr[:-1])

    # Insert the last element into the sorted prefix
    key = arr[-1]
    i = len(sorted_prefix) - 1

    while i >= 0 and sorted_prefix[i] > key:
        sorted_prefix.insert(i + 1, sorted_prefix[i])
        i -= 1

    sorted_prefix[i + 1 if i >= -1 else 0] = key

    return sorted_prefix


# Example
unsorted_list = [7, 2, 4, 1, 5, 3]
print("Original list:", unsorted_list)
print("Sorted list:", recu

