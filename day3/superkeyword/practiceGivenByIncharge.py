class manager:
    def bonus(self):
        print("Manager bonus 10000")
        
class employee(manager):
    def bonus(self):
        super().bonus()
        print("Emplloyee bonus 5000")




employee1=employee()
employee1.bonus()