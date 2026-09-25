import re

numbers = ["9876543210","12345","98765432111","1234567890","98765432101"]

pattern = r"^\d{10}$"

for number in numbers:
    if re.fullmatch(pattern, number):
        print(number, "is Valid")
    else:
        print(number, "not Invalid")