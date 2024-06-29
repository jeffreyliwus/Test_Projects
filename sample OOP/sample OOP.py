class Employee:
    totalEmployees = 0

    def __init__(self, empName, age, designation, salary):
        self.empName = empName
        self.age = age
        self.designation = designation
        self.salary = salary
        Employee.totalEmployees = Employee.totalEmployees + 1

    def getEmpDetails(self):
        return (self.empName, self.age, self.designation, self.salary)

    def updateSalary(self, newSalary):
        self.salary = newSalary
        print("Salary Updated")
        return self.salary


class Intern(Employee):
    def __init__(self, empName, age, designation, salary, internPeriod):
        self.internPeriod = internPeriod
        Employee.__init__(
            self,
            empName,
            age,
            designation,
            salary,
        )

    def getPeriod(self):
        return "intership period (in months) is: ", self.internPeriod


empOne = Employee("John", 35, "Programmer", 10000)
print(empOne.getEmpDetails())
empTwo = Employee("Sam", 24, "Manager", 5000)
print(empTwo.getEmpDetails())
empOne.updateSalary(20)
print(empOne.getEmpDetails())
print(Employee.totalEmployees)


internOne = Intern("Jerry", 24, "Marketing Manager", 40000, 12)
print(internOne.getEmpDetails())
print(internOne.getPeriod())
