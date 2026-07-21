def find_number(list_data, goal):
    low = 0
    high = len(list_data) - 1

    while low <= high:
        mid = (low + high) // 2

        if list_data[mid] == goal:
            return mid

        elif list_data[mid] < goal:
            low = mid + 1

        else:
            high = mid - 1

    return -1

# Example Use Case: (The list MUST be sorted)
numbers = [1, 5, 9, 13, 17, 21, 25]
target = 13

result = find_number(numbers, target)
print(f"Target {target} found at index: {result}")

target_not_found = 10
result_missing = find_number(numbers, target_not_found)
print(f"Target {target_not_found} found at index: {result_missing}")


def recursive_find_number(list_data, goal):
    # Base case: empty list → not found
    if len(list_data) == 0:
        return -1

    mid = len(list_data) // 2

    if list_data[mid] == goal:
        return mid

    elif goal < list_data[mid]:
        # Search left half
        return recursive_find_number(list_data[:mid], goal)

    else:
        # Search right half, but adjust index by mid+1
        result = recursive_find_number(list_data[mid + 1:], goal)
        return -1 if result == -1 else result + mid + 1


# Example Use Case
numbers = [1, 5, 9, 13, 17, 21, 25]
target = 13

result = recursive_find_number(numbers, target)
print(f"Target {target} found at index: {result}")

target_not_found = 10
result_missing = recursive_find_number(numbers, target_not_found)
print(f"Target {target_not_found} found at index: {result_missing}")

