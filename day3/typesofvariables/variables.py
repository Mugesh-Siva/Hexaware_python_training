var2="hello world"


def hello():
    print(var2)
    var="hello" # Local variable
# print(var) not valid 

count=0
def counter():
    
    global count
    count+=1
    return count
print(counter())
