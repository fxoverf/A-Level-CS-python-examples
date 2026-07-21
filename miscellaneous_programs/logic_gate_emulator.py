def logicgates():
    logicgate = input("Enter logic gate: ")
    while logicgate != 'OR' and logicgate != 'AND' and logicgate != 'XOR' and logicgate != 'NAND' and logicgate != 'NOR':
        logicgate = input("Enter logic gate: ")
    in1 = int(input("Enter first input: "))
    in2 = int(input("Enter second input: "))
    if logicgate == 'OR':
        return 1 if (in1 or in2) else 0
    elif logicgate == 'AND':
        return 1 if (in1 and in2) else 0
    elif logicgate == 'XOR':
        return 1 if (in1 != in2) else 0
    elif logicgate == 'NAND':
        return 0 if (in1 and in2) else 1
    elif logicgate == 'NOR':
        return 0 if (in1 or in2) else 1
print(f"Result = {logicgates()}")

unsortarray = [90, 26, 42, 33, 67, 51, 19, 8]
def insertionsort(array):
    for i in range(1 , len(array)):
        temp = array[i]
        s = i - 1
        print(s)
        swaps = 0
        while s >= 0  and temp > array[s]:
            array[s + 1] = array[s]
            s -= 1
            swaps += 1
            array[s + 1] = temp
        print(f"Pass {i}: Number of swaps: {swaps}")
    return array
print(f"unsorted array {unsortarray}")
print(f"sorted array: {insertionsort(unsortarray)}")