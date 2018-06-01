class Human:

    def __init__(self, first, last, gender):
        self.firstname = first
        self.lastname = last
        self.gender = gender

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Human):

    def __init__(self, first, last, gender, Id, company, salary):
        Human.__init__(self,first, last, gender)
        self.id = Id
        self.company = company
        self.salary = salary

    def GetEmployee(self):
        return [self.Name(), self.company, self.salary]

y = Employee("Dilnawaz", "Ragib", 'Male', "1007", 'Quantiphi', '1 Lakh')

sorted_employee = sorted(y.GetEmployee(), key = lambda x:x[-1], reversed = True)
