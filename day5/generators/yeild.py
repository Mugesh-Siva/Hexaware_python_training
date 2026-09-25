def even_numbers():
    yield 2
    yield 4
    yield 6
    yield 8
    yield 10
numbers= even_numbers()
print(numbers)
print(next(numbers))
print(next(numbers))

#Generator process the reocrd one at the time
# And it reduce memory usage instead of loading entire record into memory



def employee():
    yield "Mugesh"
    yield "Arun"
    yield "Akhila"

employees=employee()
for i in range(3):

    name=next(employees)
    empid=" hexaware"
    name+=empid
    #Process the name how ever you want

    print(name)