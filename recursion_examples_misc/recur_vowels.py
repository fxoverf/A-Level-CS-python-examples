def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    firstchar = Value[0]
    if firstchar == 'a' or firstchar == 'e' or firstchar == 'i' or firstchar == 'u' or firstchar == 'o':
        return 1 + RecursiveVowels(Value[1:])
    else:
        return RecursiveVowels(Value[1:])
string = input("Enter a String: ")
print(RecursiveVowels(string))