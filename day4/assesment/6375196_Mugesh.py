import mysql.connector


class InvalidSalaryError(Exception):
    pass


def connect_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="employee_db"
    )
    return connection


def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        emp_name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = int(input("Enter Salary: "))

        if salary <= 0:
            raise InvalidSalaryError("Salary must be greater than zero.")

        connection = connect_database()
        cursor = connection.cursor()

        cursor.execute("SELECT emp_id FROM employee WHERE emp_id = %s", (emp_id,))
        existing = cursor.fetchone()

        if existing:
            print("An employee with this ID already exists.")
        else:
            query = "INSERT INTO employee (emp_id, emp_name, department, salary) VALUES (%s, %s, %s, %s)"
            values = (emp_id, emp_name, department, salary)
            cursor.execute(query, values)
            connection.commit()
            print("Employee added successfully.")

    except ValueError:
        print("Invalid input. Employee ID and Salary must be numbers.")
    except InvalidSalaryError as e:
        print("Error:", e)
    except mysql.connector.Error as e:
        print("Database error:", e)
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass


def view_employees():
    try:
        connection = connect_database()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM employee")
        rows = cursor.fetchall()

        if not rows:
            print("No employee records found.")
        else:
            print("\nEmp ID | Name | Department | Salary")
            print("-" * 40)
            for row in rows:
                print(row[0], "|", row[1], "|", row[2], "|", row[3])

    except mysql.connector.Error as e:
        print("Database error:", e)
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass


def update_salary():
    try:
        emp_id = int(input("Enter Employee ID to update: "))
        new_salary = int(input("Enter New Salary: "))

        if new_salary <= 0:
            raise InvalidSalaryError("Salary must be greater than zero.")

        connection = connect_database()
        cursor = connection.cursor()

        cursor.execute("SELECT emp_id FROM employee WHERE emp_id = %s", (emp_id,))
        existing = cursor.fetchone()

        if not existing:
            print("No employee found with this ID.")
        else:
            cursor.execute("UPDATE employee SET salary = %s WHERE emp_id = %s", (new_salary, emp_id))
            connection.commit()
            print("Salary updated successfully.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except InvalidSalaryError as e:
        print("Error:", e)
    except mysql.connector.Error as e:
        print("Database error:", e)
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass


def delete_employee():
    try:
        emp_id = int(input("Enter Employee ID to delete: "))

        connection = connect_database()
        cursor = connection.cursor()

        cursor.execute("SELECT emp_id FROM employee WHERE emp_id = %s", (emp_id,))
        existing = cursor.fetchone()

        if not existing:
            print("No employee found with this ID.")
        else:
            cursor.execute("DELETE FROM employee WHERE emp_id = %s", (emp_id,))
            connection.commit()
            print("Employee deleted successfully.")

    except ValueError:
        print("Invalid input. Employee ID must be a number.")
    except mysql.connector.Error as e:
        print("Database error:", e)
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass


def export_report():
    try:
        connection = connect_database()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM employee")
        rows = cursor.fetchall()

        with open("employee_report.txt", "w") as file:
            file.write("Employee Report\n")
            file.write("=" * 40 + "\n")
            for row in rows:
                line = "ID: " + str(row[0]) + ", Name: " + row[1] + ", Department: " + row[2] + ", Salary: " + str(row[3])
                file.write(line + "\n")

        print("Report exported to employee_report.txt")

    except mysql.connector.Error as e:
        print("Database error:", e)
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass


def search_by_department():
    try:
        department = input("Enter Department to search: ")

        connection = connect_database()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM employee WHERE department = %s", (department,))
        rows = cursor.fetchall()

        if not rows:
            print("No employees found in this department.")
        else:
            for row in rows:
                print(row[0], "|", row[1], "|", row[2], "|", row[3])

    except mysql.connector.Error as e:
        print("Database error:", e)
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass


def show_total_employees():
    try:
        connection = connect_database()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM employee")
        result = cursor.fetchone()
        print("Total Employees:", result[0])

    except mysql.connector.Error as e:
        print("Database error:", e)
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass


def main():
    while True:
        print("\n----- Employee Management System -----")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Salary")
        print("4. Delete Employee")
        print("5. Export Report")
        print("6. Search by Department")
        print("7. Show Total Employees")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_salary()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            export_report()
        elif choice == "6":
            search_by_department()
        elif choice == "7":
            show_total_employees()
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()