Temp = []
high = 0
low = 1000000000
for count in range(3):
    temp = int(input(f"enter temperature of hour {count + 1}:"))
    Temp.append(temp)
    if temp > high:
        high = temp
    elif temp < low:
        low = temp

print(f"the highest entered temperature was: {high} and the lowest entered temperature was: {low}")