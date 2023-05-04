import requests

isOpen = True




def printMenu():
    pass

def addEmployee():
    print("ss")
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