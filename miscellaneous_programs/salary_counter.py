empname= []
salaries = []
mini = 50000
maxi = 200000
lengthnamemax = 15
nummin = 0
for count in range(3):
    name = input(f"enter name of employee {count + 1}:")
    while len(name) > 15:
      name = input(f"enter name of employee {count + 1}:")
      if len(name) <= 15:
          break
    empname.append(name)
    salary = int(input(f"enter salary of employee {count + 1}:"))
    while salary < mini or salary > maxi:
        salary = int(input(f"enter salary of employee {count + 1}:"))
        if mini <= salary <= maxi:
            break
    salaries.append(salary)
    if salary == mini:
        nummin = nummin + 1

print(f"the number of employees getting salary of 50000 is: {nummin}")


