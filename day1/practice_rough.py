age=18
number=23
if age==18:
    print("age is 18")
    print(age==19)

print(3*"hello world \n")
employee_name="arun"
employee_age=21

# Lists
lists=[1,2,3,4,5]
lists[0]="Mugesh"
print(lists)
#----------------------------------------------------
print("employee_name:", employee_name)
print(f"employee_age: {employee_age}")
tuples=(1,2,3,4,5)
print(tuples)

# garbage collector example
import gc
a = [1, 2, 3]
del a
gc.collect()
print("Garbage collection completed")

#python virtual environment
'''
create an virtual evironment: py -m venv myenv
run it : .\myenv\Scripts\Activate.ps1
 '''

# case and match
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")


# split usage
text = "Hello World Python Happy Birthday "
words = text.split()
print(words)