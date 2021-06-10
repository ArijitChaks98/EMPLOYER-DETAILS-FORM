class Employe:
    def __init__(self, id, name, address, designation, salary, project):
        self.id = id
        self.name = name
        self.address = address
        self.designation = designation
        self.salary = salary
        self.project = project
      
lst = []

def enterEmploye():
    id = int(input("Enter Employes Id:\n"))
    name = input("Enter Employes Name:\n")
    address = input("Enter Employes Address:\n")
    designation = input("Enter Employes Designation:\n")
    salary = int(input("Enter Employes Salary:\n"))
    project = input("Enter Employes Project Details:\n")
    lst.append(Employe(id, name, address, designation, salary, project))
    isAnother = input('press "y" to enter another record\n')
    if isAnother == "y":
        enterEmploye()
enterEmploye()

for j in lst:
    print(j.id, "|", j.name, "|", j.address, "|", j.designation, "|", j.salary, "|", j.project)