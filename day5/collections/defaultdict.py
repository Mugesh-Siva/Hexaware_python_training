from collections import defaultdict
employee=defaultdict(list)
employee["IT"].append("Arun")
employee["HR"].append("Priya")
employee["IT"].append("Karthik")
employee["FFINANCE"].append("Meena")
print(employee["IT"])
print(employee)