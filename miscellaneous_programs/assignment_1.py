arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
def linearSearch(num):
    foundnum = False
    for c in range(len(arrayData)):
        if num == arrayData[c]:
            foundnum = True
    return foundnum
def bubblesort(theArray):
    for x in range(len(theArray)):
        for y in range(len(theArray) - 1):
            if theArray[y] < theArray[y + 1]:
                temp = theArray[y]
                theArray[y] = theArray[y + 1]
                theArray[y + 1] = temp
    print(theArray)

#main program
choice = input("enter s for searching a number and b for sorting the array: ")
if choice == 's':
    searchnum = int(input("enter the number to search: "))
    found = linearSearch(searchnum)
    if found == True:
       print("the value was found in the array")
    else:
       print("the value was not found in the array")
elif choice == 'b':
    bubblesort(arrayData)