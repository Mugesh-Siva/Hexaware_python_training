def calsal(salary,id,name):
    salary=salary*1.10
    return salary,id,name
emplist=list(calsal(1000,101,"Mugesh"))
for i in range(0,len(emplist)):
    print(emplist[i],end=" ")