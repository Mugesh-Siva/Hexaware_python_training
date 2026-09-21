'''Python Assesment-1'''

# Employee details - Employee details assigned to variables
employee_id = 101
employee_name = "Arun"
department = "Analytics"
designation = "Data Analyst"
monthly_salary = 50000
bonus = 25000
is_active = True

# Salary calculations - using operators to calculate the salary and bonuses
annual_salary = monthly_salary * 12
total_compensation = annual_salary + bonus

# High earner - using comparison operator checking the employee is an high earner or not, that is stored as boolean
is_high_earner = annual_salary >= 600000

# Projects - List of projects that has one duplicate project
projects = [
    "Sales Dashboard",
    "Customer Analytics",
    "Sales Dashboard"
]

# Skills - List of Skills that has one duplicate skill
skills = [
    "Python",
    "SQL",
    "Power BI",
    "Python",
    "Git"
]

# Unique projects and skills - converting the list to set for getting unique values.
unique_projects = set(projects)
unique_skills = set(skills)

# Employee profile dictionary - creating key value pairs where the values are varibles that are already assigned.
employee = {
    "id": employee_id,
    "name": employee_name,
    "department": department,
    "designation": designation,
    "monthly_salary": monthly_salary,
    "bonus": bonus,
    "active": is_active
}

# Employee Report - The entire employee report printed here
print("================== EMPLOYEE PROFILE ==========================")
print(f"Employee ID          : {employee_id}")
print(f"Employee Name        : {employee_name}")
print(f"Department           : {department}")
print(f"Designation          : {designation}")
print(f"Monthly Salary       : {monthly_salary}")
print(f"Annual Salary        : {annual_salary}")
print(f"Bonus                : {bonus}")
print(f"Total Compensation   : {total_compensation}")
print(f"High Earner          : {is_high_earner}")
print(f"Active Status        : {is_active}")
print(f"Projects             : {projects}")
print(f"Unique Projects      : {unique_projects}")
print(f"Skills               : {skills}")
print(f"Unique Skills        : {unique_skills}")
print("=========================ENd Of The Report=========================")

#type checking as per the problem statement
print(type(employee_id))

