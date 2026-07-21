WEEK = 7
BASE = 100000
BASE2 = 500000
lessthan100k = 0
morethan500k = 0
totalnumEnq = 0
for count in range(WEEK):
    numEnq = int(input(f"enter number of customer enquiries for day {count+1} :"))
    total = 0
    totalnumEnq = totalnumEnq + numEnq
    while  total < numEnq:
        price = float(input("enter price of house: "))
        if price < BASE:
            lessthan100k = lessthan100k + 1
            total = total + 1
        elif price > BASE2:
            morethan500k = morethan500k + 1
            total = total + 1
        else:
            total = total + 1


percmorethan500k = (morethan500k / totalnumEnq) * 100

print(f"The number of customers who enquired about houses costing less than $100000 is: {lessthan100k}")
print(f"The percentage of enquiries about houses costing more than $500000 is: {percmorethan500k}%")