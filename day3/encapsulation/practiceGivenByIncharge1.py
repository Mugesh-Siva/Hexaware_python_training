class bankaccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,depositAmount):
        self.__balance+=depositAmount
        
    def getbal(self):
        return self.__balance

    
user1=bankaccount(2000)

print(user1.getbal())

user1.deposit(200)
print(user1.getbal())