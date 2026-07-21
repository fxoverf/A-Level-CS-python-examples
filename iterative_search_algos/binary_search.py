def binarysearch(searcharray, searchnum):
    lower = 0
    upper = len(searcharray) - 1
    foundnum = False
    mid = 0
    while lower <= upper and not foundnum:
        mid = int((upper + lower)/2)
        if searcharray[mid] == searchnum:
            foundnum = True
            break
        elif searcharray[mid] < searchnum:
            lower = mid + 1
        else:
            upper = mid - 1

    if foundnum:
        print(f"the number was found at {mid + 1}")
    else:
        print("the number was not found")

Numarray = [10, 20, 30 ,40 ,50 ,60]
search = int(input("enter number to search: "))
binarysearch(Numarray, search)