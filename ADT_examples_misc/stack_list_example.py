#w2025 p41 q1 9618
Stack = [None for i in range(30)]
TopOfStack = -1
def push(element):
    global TopOfStack, Stack
    if TopOfStack + 1 == len(Stack):
        return False
    else:
        TopOfStack += 1
        Stack[TopOfStack] = element
        return True
def pop():
    global TopOfStack, Stack
    if TopOfStack == -1:
        return -999
    else:
        currentValue = Stack[TopOfStack]
        TopOfStack -= 1
        return currentValue
def FindValues():
    global Stack, TopOfStack
    popVal = 0
    largestValue = -1
    smallestValue = 999
    while popVal != -999:
        stackValue = Stack[TopOfStack]
        if stackValue > largestValue:
            largestValue = stackValue
        elif stackValue < smallestValue:
            smallestValue = stackValue
        popVal = pop()
    print("Largest Value: ", largestValue)
    print("Smallest Value: ", smallestValue)

#main program
import random
for x in range(40):
    pushVal = push(random.randint(0, 1000))
    if pushVal == False:
        print("Stack Full")
        break

FindValues()