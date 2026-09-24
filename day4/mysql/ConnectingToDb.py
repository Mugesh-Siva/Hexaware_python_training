import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mugeshsiva@23",
    database="python_training"
)
cursor=db.cursor()
print("database and cursor ready")
cursor.execute("select * from employee")
data=cursor.fetchall()
for row in data:
    print(row)

print("="*49)
print("After Update")
print("="*49)

query = "UPDATE employee SET employee_name = %s WHERE id = %s"
values=("mugesh",3)
cursor.execute(query,values)

cursor.execute("select * from employee")
data=cursor.fetchall()
for row in data:
    print(row)


print("="*49)
print("After Delete")
print("="*49)

delete_query = "DELETE FROM employee WHERE id = %s"
values=(2,)
cursor.execute(delete_query,values)

cursor.execute("select * from employee")
data=cursor.fetchall()
for row in data:
    print(row)



print("="*49)
print("After Execute Many")
print("="*49)

query = "INSERT INTO employee (id, employee_name, department_id) VALUES (%s, %s, %s)"
values=[
    (4,'Anish', 101),
    (5,'Kavya', 103),
    (6,'Vikram', 102)
]

cursor.executemany(query,values)
db.commit()
cursor.execute("select * from employee")
data=cursor.fetchall()
for row in data:
    print(row)




cursor.close()


db.close()