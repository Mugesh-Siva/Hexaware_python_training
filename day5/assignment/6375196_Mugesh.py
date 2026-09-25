import re
import time
import unittest
from collections import Counter


class InvalidEmployeeError(Exception):
    pass


EMP_ID_PATTERN = r'^EMP\d{4}$'
NAME_PATTERN = r'^[A-Za-z ]+$'


def is_valid_emp_id(emp_id):
    return bool(re.match(EMP_ID_PATTERN, emp_id))


def is_valid_name(name):
    return bool(re.match(NAME_PATTERN, name))


def validate_employee(employee):
    emp_id = employee.get('emp_id', '')
    name = employee.get('name', '')
    department = employee.get('department', '')
    salary = employee.get('salary', 0)

    if not is_valid_emp_id(emp_id):
        raise InvalidEmployeeError(f"Invalid employee ID: {emp_id}")

    if not is_valid_name(name):
        raise InvalidEmployeeError(f"Invalid employee name: {name}")

    if not department:
        raise InvalidEmployeeError(f"Department cannot be empty for {emp_id}")

    if salary <= 0:
        raise InvalidEmployeeError(f"Salary must be greater than 0 for {emp_id}")

    return True


def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Starting execution: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished execution: {func.__name__}")
        return result
    wrapper.__name__ = func.__name__
    return wrapper


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    wrapper.__name__ = func.__name__
    return wrapper


def calculate_bonus(salary):
    if salary >= 60000:
        return salary * 0.15
    return salary * 0.10


def process_employees(employees):
    for employee in employees:
        try:
            validate_employee(employee)
        except InvalidEmployeeError as error:
            print(f"Skipping record: {error}")
            continue

        bonus = calculate_bonus(employee['salary'])
        processed_employee = {
            'emp_id': employee['emp_id'],
            'name': employee['name'],
            'department': employee['department'],
            'salary': employee['salary'],
            'bonus': bonus
        }
        yield processed_employee


class EmployeeAnalytics:
    def __init__(self):
        self.valid_employees = []
        self.department_counter = Counter()

    def add_employee(self, employee):
        self.valid_employees.append(employee)
        self.department_counter[employee['department']] += 1

    def total_salary(self):
        return sum(employee['salary'] for employee in self.valid_employees)

    def total_bonus(self):
        return sum(employee['bonus'] for employee in self.valid_employees)

    def average_salary(self):
        if not self.valid_employees:
            return 0
        return self.total_salary() / len(self.valid_employees)

    def highest_salary(self):
        if not self.valid_employees:
            return 0
        return max(employee['salary'] for employee in self.valid_employees)

    def lowest_salary(self):
        if not self.valid_employees:
            return 0
        return min(employee['salary'] for employee in self.valid_employees)

    def department_summary(self):
        return dict(self.department_counter)

    def highest_bonus_employees(self):
        if not self.valid_employees:
            return []
        max_bonus = max(employee['bonus'] for employee in self.valid_employees)
        return [employee for employee in self.valid_employees if employee['bonus'] == max_bonus]


def write_report(analytics, file_path):
    with open(file_path, 'w') as report_file:
        report_file.write("Employee Analytics Report\n")
        report_file.write("-------------------------\n")
        report_file.write(f"Valid Employees: {len(analytics.valid_employees)}\n")
        report_file.write(f"Total Salary: {analytics.total_salary()}\n")
        report_file.write(f"Total Bonus: {analytics.total_bonus()}\n")
        report_file.write(f"Average Salary: {analytics.average_salary():.2f}\n")
        report_file.write(f"Highest Salary: {analytics.highest_salary()}\n")
        report_file.write(f"Lowest Salary: {analytics.lowest_salary()}\n")
        report_file.write(f"Department Summary: {analytics.department_summary()}\n")


@log_execution
@measure_time
def run_analytics_engine(employees, report_path):
    analytics = EmployeeAnalytics()
    for processed_employee in process_employees(employees):
        analytics.add_employee(processed_employee)
    write_report(analytics, report_path)
    return analytics


class TestEmployeeAnalytics(unittest.TestCase):

    def test_valid_employee_id(self):
        self.assertTrue(is_valid_emp_id("EMP1001"))

    def test_invalid_employee_id(self):
        self.assertFalse(is_valid_emp_id("BAD01"))

    def test_valid_employee_name(self):
        self.assertTrue(is_valid_name("Arun Kumar"))

    def test_invalid_employee_name(self):
        self.assertFalse(is_valid_name("Karthik123"))

    def test_correct_bonus_at_salary_60000(self):
        self.assertEqual(calculate_bonus(60000), 9000.0)

    def test_invalid_negative_salary(self):
        employee = {
            "emp_id": "EMP1005",
            "name": "Rahul",
            "department": "IT",
            "salary": -5000
        }
        with self.assertRaises(InvalidEmployeeError):
            validate_employee(employee)


if __name__ == '__main__':
    sample_employees = [
        {"emp_id": "EMP1001", "name": "Arun Kumar", "department": "IT", "salary": 65000},
        {"emp_id": "EMP1002", "name": "Priya Sharma", "department": "HR", "salary": 55000},
        {"emp_id": "EMP1003", "name": "Karthik123", "department": "IT", "salary": 70000},
        {"emp_id": "EMP1004", "name": "Meena Raj", "department": "Finance", "salary": 80000},
        {"emp_id": "EMP1005", "name": "Rahul", "department": "IT", "salary": -5000},
        {"emp_id": "BAD01", "name": "Divya Kumar", "department": "HR", "salary": 60000}
    ]

    run_analytics_engine(sample_employees, "employee_report.txt")

    print("\nRunning unit tests...\n")
    unittest.main(argv=[''], exit=False, verbosity=2)