# Dummy Data for the employeees copied directly from the problem statement
employees = [
    {
        "name": "  Arun Kumar ",
        "department": "Analytics",
        "salary": 58000,
        "score": 86,
        "attendance": 92,
        "skills": ["Python", "SQL", "Python", "Power BI"],
        "active": True
    },
    {
        "name": "Priya Sharma",
        "department": "HR",
        "salary": 45000,
        "score": 74,
        "attendance": 88,
        "skills": ["Excel", "Communication", "Excel"],
        "active": True
    },
    {
        "name": " Karthik Raj ",
        "department": "IT",
        "salary": 65000,
        "score": 95,
        "attendance": 96,
        "skills": ["Python", "Cloud", "SQL", "Python"],
        "active": True
    },
    {
        "name": "Meena Joseph",
        "department": "Analytics",
        "salary": 49000,
        "score": 61,
        "attendance": 72,
        "skills": ["SQL", "Excel", "SQL"],
        "active": True
    },
    {
        "name": "Rahul Das",
        "department": "IT",
        "salary": 52000,
        "score": 42,
        "attendance": 81,
        "skills": ["Cloud", "Linux", "Cloud"],
        "active": False
    },
    {
        "name": "  Swetha R ",
        "department": "HR",
        "salary": 55000,
        "score": 68,
        "attendance": 79,
        "skills": ["Python", "Communication", "Python"],
        "active": True
    }
]

# REQUIREMENT 1 - CLEAN EMPLOYEE DATA
# I am using strip to remove the leading and trailing spaces in the name and save it in the name
# iam using upper() to convert the department into upper case and save it in the department
for emp in employees:
    emp["name"] = emp["name"].strip()
    emp["department"] = emp["department"].upper()

# REQUIREMENT 2 - PERFORMANCE RATING
# Iam using nested If with else if ladder to check the performance with the score and add rating to them
for emp in employees:
    if emp["active"]:
        score = emp["score"]
        if score >= 90:
            emp["rating"] = "Excellent"
        elif score >= 75:
            emp["rating"] = "Good"
        elif score >= 50:
            emp["rating"] = "Needs Improvement"
        else:
            emp["rating"] = "Poor"

# REQUIREMENT 3 - BONUS ELIGIBILITY
# Using "and" with if else to check for multiple conditions for the bonus eligibility
for emp in employees:
    if emp["active"] and emp["attendance"] >= 85 and emp["salary"] >= 50000:
        emp["bonus"] = "Eligible"
    else:
        emp["bonus"] = "Not Eligible"

# REQUIREMENT 4 - UNIQUE SKILLS
# some employees registered duplicate skills and removing that using set implementation
for emp in employees:
    emp["unique_skills"] = set(emp["skills"])

# REQUIREMENT 5 - NESTED LOOP SKILL ANALYSIS
# Creating an set to get the unique skills for the analytics and it skills in employees
# the first loop loops all the employees and the if condition checks the department is analytics or it
# and the second loop inside the if statements will add those skills to the set so set naturally removes duplicates
analytics_skills = set()
it_skills = set()
for emp in employees:
    if emp["department"] == "ANALYTICS":
        for skill in emp["unique_skills"]:
            analytics_skills.add(skill)
    if emp["department"] == "IT":
        for skill in emp["unique_skills"]:
            it_skills.add(skill)

common_skills = set()
for skill in analytics_skills:
    if skill in it_skills:
        common_skills.add(skill)

# REQUIREMENT 6&7 department summary and use continue
# using continue to skipping the not active employees
department_count = {}
for emp in employees:
    if not emp["active"]:
        continue
    dept = emp["department"]
    if dept in department_count:
        department_count[dept] = department_count[dept] + 1
    else:
        department_count[dept] = 1

# REQUIREMENT 8 - USE BREAK
# finding the first employee who scores below 50 and breaks the entire loop
first_low_scorer = None
for emp in employees:
    if not emp["active"]:
        continue
    if emp["score"] < 50:
        first_low_scorer = emp["name"]
        break

# REQUIREMENT 9 - SALARY REVISION USING map()
#using lambda functin and increase the salary of the employees by 10 percent by adding the existing salaries of the employees in a list and using map to process them.
original_salaries = []
for emp in employees:
    original_salaries.append(emp["salary"])

revised_salaries = list(map(lambda s: s * 1.10, original_salaries))

# REQUIREMENT 10 - USER INPUT SEARCH
# gets input from the department and then converts it to upper because the all the departments are already in upper
search_department = input("Enter department to search: ")
search_department = search_department.upper()

# REQUIREMENT 11 - FINAL REPORT
print("=" * 40)
print("EMPLOYEE PERFORMANCE REPORT")
print("=" * 40)
print()
# using for loop repetition to print all the values of the employee 
for emp in employees:
    if emp["active"]:
        print("Name       :", emp["name"])
        print("Department :", emp["department"])
        print("Score      :", emp["score"])
        print("Attendance :", emp["attendance"])
        print("Rating     :", emp["rating"])
        print("Bonus      :", emp["bonus"])
        print("Skills     :", emp["unique_skills"])
        print()

print("=" * 40)
print("DEPARTMENT SUMMARY")
print("=" * 40)
print()
for dept in department_count:
    print(dept, ":", department_count[dept])
print()

print("=" * 40)
print("COMMON ANALYTICS-IT SKILLS")
print("=" * 40)
print()
print(common_skills)
print()

print("=" * 40)
print("SALARY REVISION")
print("=" * 40)
print()
print("Original Salaries:")
print(original_salaries)
print()
print("Revised Salaries:")
print(revised_salaries)
print()

print("=" * 40)
print("FIRST ACTIVE EMPLOYEE BELOW 50")
print("=" * 40)
print()
if first_low_scorer is not None:
    print(first_low_scorer)
else:
    print("Not Found")
print()

print("=" * 40)
print("SEARCH RESULT FOR DEPARTMENT:", search_department)
print("=" * 40)
print()
# this is the display part of requirement 10
# This loop searches the department entered via input and then search all the employees and prints it
for emp in employees:
    if emp["active"] and emp["department"] == search_department:
        print(emp["name"], "-", emp["department"])
print()

# BONUS CHALLENGE - max() and min() 
# using max() and min() to find the highest and lowest salary
highest_salary = max(original_salaries)
lowest_salary = min(original_salaries)
print("Highest Salary :", highest_salary)
print("Lowest Salary  :", lowest_salary)
print()


# BONUS 2 - HIGHEST SCORE
# displaying the top scored employee from the from loop setting the initial value as emp[0] and iterating to the list
top_scorer = employees[0]
for emp in employees:
    if emp["score"] > top_scorer["score"]:
        top_scorer = emp
print("Employee with Highest Score:", top_scorer["name"], "-", top_scorer["score"])