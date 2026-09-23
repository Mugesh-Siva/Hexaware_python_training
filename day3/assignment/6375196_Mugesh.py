
class Employee:

    company_name = "ABC Organisation"

    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def calculate_bonus(self):
        return self.__salary * 0.10

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.get_salary())
        print("Bonus:", self.calculate_bonus())

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0

    @classmethod
    def show_company(cls):
        print("Company:", cls.company_name)


class Manager(Employee):

    def __init__(self, employee_id, name, department, salary, team_size):
        super().__init__(employee_id, name, department, salary)
        self.team_size = team_size

    def calculate_bonus(self):
        return self.get_salary() * 0.20

    def display_details(self):
        print("Manager ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.get_salary())
        print("Team Size:", self.team_size)
        print("Bonus:", self.calculate_bonus())


Employee.show_company()

employee1 = Employee(101, "Arun", "Analytics", 60000)
manager1 = Manager(201, "Priya", "HR", 80000, 5)

print("\nEmployee Details")
employee1.display_details()

print("\nManager Details")
manager1.display_details()

print("\nSalary Validation")
print(Employee.is_valid_salary(60000))
print(Employee.is_valid_salary(-5000))

print("\nPolymorphism")

employees = [employee1, manager1]

for employee in employees:
    print(employee.name, "Bonus:", employee.calculate_bonus())

print("\nSalary Encapsulation")
print("Arun Salary:", employee1.get_salary())
