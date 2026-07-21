import random
R = []
def RandomNumber():
    for i in range(10):
        num = random.randint(0, 200)
        R.append(num)
    print(f"Random numbers are: {R}")
RandomNumber()

def bubblesort(unsort):
    temp = 0
    count = 0
    swap = False
    while count < len(R) and not swap:
        swap = True
        for i in range(len(R) - 1):
            if R[i] > R[i + 1]:
                temp = R[i]
                R[i] = R[i + 1]
                R[i + 1] = temp
                swap = False
        count += 1
    print(f"sorted array: {R}")
bubblesort(R)

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
search = int(input("enter number to search: "))
binarysearch(R, search)