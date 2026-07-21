#inertion sort function
def insertionsort(array):
    for i in range(1 , len(array)):
        temp = array[i]
        s = i - 1
        while s >= 0  and temp < array[s]:
            array[s + 1] = array[s]
            s = s - 1
            array[s + 1] = temp
    return array
#main program
unsortarray = [20, 4, 30 ,10, 56]
print(f"unsorted array {unsortarray}")
insertionsort(unsortarray)
print(f"sorted array: {unsortarray}") #array passed by reference