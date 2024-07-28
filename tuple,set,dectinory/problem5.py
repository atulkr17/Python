'''
Shortlist Students for a Job role
Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.

Show every students record in form of tuples if matches all required criteria.

It is assumed that there will be only one primry skill.

If no such candidate found, print No such candidate

Input:

Enter No of records- 2
Enter Details of student-1
Enter Student name- Manohar
Enter Higher Education- B.Tech
Enter Primary Skill- Python
Enter Year of Graduation- 2022
Enter Details of student-2
Enter Student name- Ponian
Enter Higher Education- B.Sc.
Enter Primary Skill- C++
Enter Year of Graduation- 2020

Enter Job Role Requirement
Enter Skill- Python
Enter Higher Education- B.Tech
Enter Year of Graduation- 2022
Output

('Manohar', 'B.tech', 'Python', '2022')

'''
student=[]
num=int(input("Enter a number"))

for i in range(num):
    print("enter datals of ",i+1,"applicant")
    name=input("Enter name")
    h_ed=input("Enter Higher Education")
    p_skill=input("primary skill")
    yog=input("Enter of year of Graduation")
    student.append((name,h_ed,p_skill,yog))

requride_skill=input("Enter Skill")    
requride_HE=input("Enter higher education")
requride_YOG=input("Enter year of graducation")
flag=True
for i in student:
    if i[1]==requride_HE and i[2]==requride_skill and i[3]==requride_YOG:
        print(i)
        flag=False
if flag:
    print("no such'")        

