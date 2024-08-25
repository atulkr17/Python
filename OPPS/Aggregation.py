class Customer:

    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def printAddress(self):
        print(self.address.get_city(),self.address.pin,self.address.state)   

    def EditeAddress(self,new_city,new_pin,new_state):
        self.address.edite_address(new_city,new_pin,new_state)   


class Address:

    def __init__(self,city,pin,state):

        self.__city=city
        self.pin=pin
        self.state=state

    def get_city(self):
        return self.__city    
    
    def edite_address(self,new_city,new_pin,new_state):
        self.__city=new_city
        self.pin=new_pin
        self.state=new_state


addr=Address('Patna',84122,'Bihar')
cust=Customer('Atul','Male',addr)
cust.printAddress()
addr.edite_address('saran',1234,'kolkata')
cust=Customer('Atul','Male',addr)
cust.printAddress()
