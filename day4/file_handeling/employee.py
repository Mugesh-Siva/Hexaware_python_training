def add_employee(name,department,salary):
    with open("employee.txt","a") as file:
        file.write(f"{name},{department},{salary}\n")
def show_employees():
    with open ("employee.txt","r") as file:
        data=file.readlines()
        print(data)
add_employee ("swathi","HR",65000)
add_employee ("priya","IT","50000")

show_employees()