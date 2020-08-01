from employee import employee

def main():
    data = {"name":"Nathalia","lastName":"Calzado","gender":"Female","status":"contractor","yrsExp":4,"title":"System Administrator"}
    emp = employee(data)

    print(emp.salary)

if __name__ == "__main__":
    main()