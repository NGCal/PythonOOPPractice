from employee import employee
from mimesis import Person
from mimesis.enums import Gender
from pandas import DataFrame
from random import randrange

def generatePple(options,plpAmnt):

    person = Person('en')
    df = DataFrame(columns=["name","lastName","gender","title","status","yrsExp","salary","lastBonus"])
    print(df)

    while plpAmnt > 0:

        gender = options["GENDER"][randrange(0,len(options["GENDER"]))]
        title = options["TITLES"][randrange(0,len(options["TITLES"]))]
        status = options["STATUS"][randrange(0,len(options["STATUS"]))]

        data = {
           "name": person.name(gender=Gender[gender]),
           "lastName": person.last_name(gender=Gender[gender]),
           "gender":gender,
           "status":status,
           "title":title,
           "yrsExp":randrange(0,15)
        }

        empObj = employee(data)
        data["salary"] = empObj.salary
        data["lastBonus"] = empObj.lastBonus

        df = df.append(data,ignore_index=True)
        

        plpAmnt = plpAmnt - 1

    return df

def main():
    options = {"GENDER":["FEMALE", "MALE"],"TITLES":["MANAGER","DEVELOPER","SYSTEM ADMINISTRATOR","RECRUITER"],"STATUS":["CONTRACTOR","EMPLOYEE"]}
    
    employees = generatePple(options,25)

    print(employees)
    

if __name__ == "__main__":
    main()