import requests

isOpen = True




def printMenu():
    pass

def addEmployee():
    details=input("Please enter: (id, firs name, last name,gender, age,salary,mail)").split(",")
    newEmp=Employee(int(details[0]),details[1],details[2],details[3],float(details[4]),float(details[5]),details[6])
    newEmpJson = json.dumps(newEmp)
    requests.post(url+'/addEmployee',json=newEmpJson)
def getEmployeeById():
    pass
def getEmployeeByName():
    pass
def getAllEmployees():
    pass
def updateEmployee():
    pass
def deleteEmployee():
    pass
def importEmployeesFromCsv():
    pass
def exportEmployeesToCsv():
    pass


functions = {
    0: testServer,
    1: addEmployee,
    2: getEmployeeById,
    3: getEmployeeByName,
    4: getAllEmployees,
    5: updateEmployee,
    6: deleteEmployee,
    7: importEmployeesFromCsv,
    8: exportEmployeesToCsv,
    9: exit
}
def main():
    print("Welcome")
    while(isOpen):
        printMenu()
        choice = int(input())

if __name__ == "__main__":
    main()