'''
TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is identified by name, technology 
skills, experience and average feedback. An instructor is allocated a course, if he/she satisfies the below two conditions:

eligibility criteria:
if experience is more than 3 years, average feedback should be 4.5 or more
if experience is 3 years or less, average feedback should be 4 or more
he/she should posses the technology skill for the course
Identify the class name and attributes to represent instructors. Write a Python program to implement the class chosen with its attributes
 and methods.

Note:

Consider all instance variables to be private and methods to be public.
An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor. Else, 
return false.
Represent a few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.


[ ]


'''
class Instructor:

    def __init__(self,name,technology,experience,feedback):
        self.name=name
        self.technology=technology
        self.experience=experience
        self.feedback=feedback

    def chake_eligibility(self):

        if self.experience >3  and self.feedback > 4.5:
            return True
        elif self.experience <= 3 and self.feedback > 4:
            return  True
        else:
            return False
 
    def allocate_course(self,tech):
        is_eligibility=self.chake_eligibility()

        if is_eligibility:
            if tech in self.technology:
                return 'padha sakta h '
            else:
                return 'pata hi nhii h usako'
            
        else:
            return 'achha nhii padhata h'   
        

ins = Instructor('Atul','Web Development',5,4.9)
print(ins.allocate_course('Web Development'))        