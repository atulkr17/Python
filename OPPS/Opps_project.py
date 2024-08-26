import nlpcloud
class NLPApp:

    def __init__(self):

        self.__databse={}
        print("i am atul")
        self.__first_menu()

    def __first_menu(self):

        first_value=input("""
         Hii! how woude you like to proceed?
          1. Not a mumber ?Register
          2. Already a mumber? loging
          3. Galti se ho gya . EXIT()                                                   
          """)    
        
        if first_value=='1':
            self.__register()
        elif first_value=='2':
            self.__loging()
        else:
            exit()        


    def __second_menu(self):

        second_value=input("""
         Hii! how woude you like to proceed?
          1. NER
          2. language Detection
          3. Sentiment Analysis
          4. loging                                                                  
          """)    
        
        if second_value=='1':
            self.__ner()
        elif second_value=='2':
            self.__language_detection()
        elif second_value=='3':
            self.__sentiment_analysis()
        else:    
            exit()                
        
    def __register(self):
        
        name=input("Enter a name")
        email=input("Entare a Email")
        password=input("Enter a password")

        if email in self.__databse:
            print("Email alredy exit")

        else:
            self.__databse[email]=[name,password]
            print("Resistation succesfully. now loging")  
            print(self.__databse)
            self.__first_menu() 

    def __loging(self):

        email=input("Enter a email")
        password=input("Enter a password")

        if email in self.__databse:
            if self.__databse[email][1]==password:
                print("loging successfully")
                self.__second_menu()
            else:
                print("Wrong password")
                self.__loging()    
        else:
            print("Email not registered")


    
    def __sentiment_analysis(self):
        para = input('enter the paragraph')

        client = nlpcloud.Client("distilbert-base-uncased-emotion", "2b58d7fb9af09e617ee525e78c7766b6d8c5bb61", gpu=False, lang="en")
        response = client.sentiment(para)

        L = []
        for i in response['scored_labels']:
            L.append(i['score'])

        index = sorted(list(enumerate(L)),key=lambda x:x[1],reverse=True)[0][0]

        print(response['scored_labels'][index]['label'])
        self.__second_menu()

obj = NLPApp()
 