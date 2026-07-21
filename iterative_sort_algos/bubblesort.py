def bubblesort(array):
    temp = 0
    count = 1
    swap = True
    while swap or count < len(array):
        for c in range(len(array) - 1):
            swap = False
            if array[c] > array[c + 1]:
                temp = array[c]
                array[c] = array[c + 1]
                array[c + 1] = temp
                swap = True
        count = count + 1
    print(f"sorted list: {array}")

#main program
num = [23, 2, 10 ,40, 5, 8, 9, 12, 81]
print(f"unsorted list: {num}")
bubblesort(num)




