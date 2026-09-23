class employee:
    def __init__(self,salary):
        self.__salary=salary
    def getsal(self):
        return self.__salary
    def setsal(self,salary):
        self.__salary=salary
employee1=employee(1000)
print(employee1.getsal())
employee1.setsal(2000)
print(employee1.getsal())

