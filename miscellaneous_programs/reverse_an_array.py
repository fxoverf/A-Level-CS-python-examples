Numbers = [1, 2, 3, 4, 5, 6]
new = [0,0,0,0,0,0]
opp = len(Numbers) - 1
for i in range(6):
    new[i] = Numbers[opp]
    opp -= 1
print(new)
