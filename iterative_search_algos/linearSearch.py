arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
def linearsearch():
    numsearch = int(input("Enter the number to search:"))
    foundnum = False
    index = 0
    while not foundnum and index != 10:
        if arrayData[index] == numsearch:
            foundnum = True
            index += 1
        else:
            index += 1
    if foundnum:
        print(f"the index at which the number was found is: {index}")
    else:
        print("the number was not found in the array")

linearsearch()