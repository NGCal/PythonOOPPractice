from employee import employee
from mimesis import Person
from mimesis.enums import Gender
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
from random import randrange

def generatePple(options,plpAmnt):

    person = Person('en')
    df = DataFrame(columns=["name","lastName","gender","title","status","yrsExp","salary","lastBonus"])

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

def generatePlot1(emplDF):
     
    emplDF = emplDF.groupby("title")["salary"].mean()
    graph = emplDF.plot(title = "Tittle vs Salary")
    graph.set_xlabel("Title")
    graph.set_ylabel("Salary")

def generatePlot2(emplDF):
    fig, ax = plt.subplots(figsize=(18,6))
    #graph = emplDF.groupby("title").plot(x="yrsExp",y="salary",ax=ax)

    for name, group in emplDF.groupby("title"):
        graph = group.plot(x="yrsExp", y='salary', ax=ax, label=name, title="Salary vs Years of Experience by Title")
    
    graph.set_xlabel("Years of Experience")
    graph.set_ylabel("Salary")
def main():
    options = {"GENDER":["FEMALE", "MALE"],"TITLES":["MANAGER","DEVELOPER","SYSTEM ADMINISTRATOR","RECRUITER"],"STATUS":["CONTRACTOR","EMPLOYEE"]}
    
    employees = generatePple(options,25)

    employees = employees.sort_values(by=["title","salary"])
    print(employees)

    generatePlot1(employees)
    generatePlot2(employees)

    plt.show()


    

if __name__ == "__main__":
    main()