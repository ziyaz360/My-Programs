##class phone:
##    model=""
##    releasedate=""
##    cost=0
##android=phone()
##android.model="Vivo T1"
##android.releasedate="22/08/22"
##android.cost=15000
##apple=phone()
##apple.model="iphone16"
##apple.releasedate="22/08/24"
##apple.cost=150000
##print(f"I am having an android phone, the model is {android.model} it was released in {android.releasedate} and it costs around {android.cost}")
##print(f"I am having an iphone, the model is {apple.model} it was released in {apple.releasedate} and it costs around {apple.cost}")
# define a class
class Employee:
    # define a property
    employee_id = 0

# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access property using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# access properties using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")
