
from titles import Titles
class employee():

    def __init__ (self, data):
        self.name = str(data['name'])
        self.lastName = str(data['lastName'])
        self.gender = str(data['gender'])
        self.title = str(data['title']).replace(" ","").upper()
        self.status = str(data['status'])
        self.yrsExp = float(data['yrsExp'])
        self.lastBonus = 0.00
        self.salary = self.calcSalary()
    
    def calcSalary(self):
        salary = 50000.00
        localTitle = self.title

        if localTitle in Titles.__members__:
            salary = Titles[localTitle].value

        expBonus = 1 + (self.yrsExp / 50.0)
        salary = salary * expBonus
        return salary

        