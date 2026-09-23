class Employee:
    company = "ABC"
    @classmethod
    def show_company(cls):
        print(cls.company)

Employee.show_company()