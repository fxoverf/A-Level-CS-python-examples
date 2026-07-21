class Employee:
    __EmployeeName = None
    __EmployeeId = int(0)

    def __init__(self, Name, Id):
        self.__EmployeeId = Id
        self.__EmployeeName = Name
    def displaydata (self):
        x = str("")
        x = f"{self.__EmployeeName} {self.__EmployeeId}"
        return x
Name = input("Enter Employee name ")
Id = input("Enter Employee Id")
Employee1 = Employee(Name, Id)
print("Employee Details")
print(Employee1.displaydata())
