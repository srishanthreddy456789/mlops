#initiate a class
class Employee:
    #special function- constructor
    def __init__(self):
        self.id=456
        self.salary=1500000
        self.designation="sde"
    def travel(self,destination):
        print(f"I am travelling to {destination}")

#creating object/instance of class
sam=Employee()
# print(sam.salary)
sam.travel("bangalore")