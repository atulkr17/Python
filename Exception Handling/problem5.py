class  InvalidAge (Exception):
  def display(self):
    print("Serrow!! your age is bellow 18g!! you come after 18 years old")
class InvalidName(Exception):
  def display(self):
    print("Your name is not valide")
try:
    name=input("Enter a name")
    if len(name)==0 or len(name.split())<2:
      raise InvalidName 
    age=int(input("Enter a number"))  
    if age<18:
      raise InvalidAge 
except InvalidName as i  :
    i.display()  
except InvalidAge as i1:
    i1.display()
else:
    print("your voat is accepited")
finally:
    print('Thank you')    
