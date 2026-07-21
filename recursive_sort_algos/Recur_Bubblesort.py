def Iterativebubble_sort(arr):
    n = len(arr)
    # n-1 passes are needed
    for i in range(n - 1):
        swapped = False
        # Compare elements up to n-i-1 (as last i elements are sorted)
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Optimization: If no two elements were swapped, list is sorted
        if not swapped:
            break
    return arr

# Example
data = [50, 20, 40, 10, 30]
print(f"Sorted: {bubble_sort(data)}")


def recursive_bubble_sort(arr):
    swapped = False
    n = len(arr)

    # One bubble pass
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True

    # If no swap → array is sorted
    if not swapped:
        return arr

    # Otherwise, recursive call again (n always = len(arr))
    return recursive_bubble_sort(arr)


# Example
data = [50, 20, 40, 10, 30]
print("Sorted:", recursive_bubble_sort(data))

