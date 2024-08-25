class user:

    def __init__(self):
        self.name='Atul kumar'

    def loging(self):
        print("loging succesfully")   

class Student(user):


    def Enrolement(self):
        print('enroll into the course')

S=Student()

print(S.name)