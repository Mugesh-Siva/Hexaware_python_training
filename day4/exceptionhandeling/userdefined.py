class UnderAge(Exception):
    pass
def checkAge(age):
    if age<18:      
        raise UnderAge("Go watch chutti tv")
try:
    checkAge(17)
except UnderAge as e:
    print(e)
except ZeroDivisionError:
    print("Unkown error occured universal level threat found")
else: #When no exception occured this else block is executed
    print("You are above 18 but still a kid ha ha")
finally: #What ever happens this block will execute at the end
    print("I dont know weather you are under or above 18 but you are in finally block")

def otherexceptions():
    try:
        number=[1,2,3]
        number[4]
    except Exception as e:
        print(e.with_traceback)
otherexceptions()