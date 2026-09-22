employees=["a","b","c"]
for employee in employees:
    if employee=="b":
        break
    print(employee)


for employee in employees:
    if employee=="b":
        continue
    print(employee)


#pass
for employee in employees:
    pass
print("Entire loop passed")