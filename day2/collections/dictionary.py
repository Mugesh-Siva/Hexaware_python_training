employeedict={
    "id":101,
    "name":"mugesh",
    "rollno":6375196,
    "salary":15000.00

}
print(employeedict.get("id"))


id=employeedict.pop("id")
print(id)

employeedict.popitem()
print(employeedict)

#insert
employeedict["name"]="mugesh siva"
print(employeedict)

print(employeedict.keys())
print(employeedict.values())
print(employeedict.items())


#setdefault() is mainly used when you want to make sure a key exists, while keeping its existing value if it already exists.

#cleared the entire list
employeedict.clear()
print(employeedict)
