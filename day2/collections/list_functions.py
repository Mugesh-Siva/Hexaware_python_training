projects = ["Banking App", "E-Commerce", "Hospital Management", "Inventory System", "Employee Portal"]

projects.append("hello")
projects.insert(1,"hello")
projects.extend(["a","b","c"])
projects.remove("a") # remove by value
last=projects.pop() #pop removes and returns an item

print(projects.index("hello")) #Its only returns the first occurance of the hello 

print(projects.count("hello")) #counts the number of times hello appeared in the list

print(f"The Last element poped is: {last}")

print(f"The Entire List: {projects}")
