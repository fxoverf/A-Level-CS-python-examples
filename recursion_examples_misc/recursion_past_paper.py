#9618 mj 2024 p42 Q3
def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, (NumberElements - 1))
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False

    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem = CheckItem - 1
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

def IterativeInsertion(IntegerArray, NumberElements):
    while NumberElements > 0:
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
        LoopAgain = True
        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
        while LoopAgain:
            IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
            CheckItem = CheckItem - 1
            if CheckItem < 0:
                LoopAgain = False
            elif IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
        IntegerArray[CheckItem + 1] = LastItem
        NumberElements = NumberElements - 1
    return IntegerArray

def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    else:
        Middle = int((Last + First) / 2)
        if IntegerArray[Middle] == ToFind:
            return Middle
        elif IntegerArray[Middle] > ToFind:
            return BinarySearch(IntegerArray, First, Middle - 1, ToFind)
        else:
            return BinarySearch(IntegerArray, Middle + 1, Last, ToFind)

#main program
NumberArray = [100, 85, 644, 22, 15, 8, 1]
print("Recursive")
print(RecursiveInsertion(NumberArray, len(NumberArray)))
print("Iterative")
print(IterativeInsertion(NumberArray, len(NumberArray)))
Position = BinarySearch(NumberArray, 0, len(NumberArray)-1, 85)
if Position == -1:
 print("Not found")
else:
 print(Position)