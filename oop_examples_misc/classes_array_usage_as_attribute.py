class Student:
    def __init__(self,name="",gr=""):
        self.name=name
        self.grades=gr
    def add_grade(self, grade):
        self.grades.append(grade)
    def getAvgGrade(self):
        if not self.grades:
            return 0
        return sum(self.grades)/len(self.grades)

name = input("Enter Student Name: ")
gradenum = int(input("Enter Number of Grades: "))
gradearr = []
for i in range(gradenum):
    grade = int(input("Enter Grade: "))
    gradearr.append(grade)

student = Student(name,gradearr)
choice = input("Would you like to add another grade? (y/n): ")
if choice == "y":
    newgrade = int(input("Enter new Grade: "))
    student.add_grade(newgrade)
    print(f"{student.name}'s grades after adding new one: {student.grades}")
    print(f"{student.name}'s average grade: {student.getAvgGrade():.2f}")
elif choice == "n":
    print(f"{student.name}'s average grade: {student.getAvgGrade()}")
