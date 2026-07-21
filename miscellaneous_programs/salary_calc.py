def salaryappraisal(newSalary, workHours):
    if workHours >= 40 and workHours <= 45:
        newSalary = newSalary * (1 + 7 / 100)
    elif workHours >= 46 and workHours <= 50:
         newSalary = newSalary * (1 + 10 / 100)
    return int(newSalary)
#main program
workingHours = int(input("enter working hours of employee:"))
basicSalary = int(input("enter salary of employee:"))
basicSalary = salaryappraisal(basicSalary, workingHours)
print(f"new salary is: {basicSalary}")


