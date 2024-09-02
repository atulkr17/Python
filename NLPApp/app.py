
from tkinter import *

from Mydb import Database

from tkinter import messagebox



class NLPAPP:

   def __init__(self):

       self.dbo=Database()
       self.root= Tk()
       self.root.title('NLPApp')
       self.root.iconbitmap('resource/android-icon-36x36.png')
       self.root.geometry('350x600')
       self.root.config(bg='#a93226')

       self.loging_gui()

       self.root.mainloop()

   def loging_gui(self):
      self.clear()

      heading=Label(self.root,text='NLPApp',bg='#a93226',fg='white')
      heading.pack(pady=(30,30))
      heading.config(font=('verdana', 24,'bold'))

      lable1=Label(self.root,text='Enter Email')
      lable1.pack(pady=(10,10))

      self.email_input = Entry(self.root,width=30)
      self.email_input.pack(pady=(5,10),ipady=4)

      lable2 = Label(self.root, text='Enter password')
      lable2.pack(pady=(10, 10))

      self.password_input = Entry(self.root, width=30,show='*')
      self.password_input.pack(pady=(5, 10), ipady=4)

      loging_but=Button(self.root,text='Login',width=30,height=2,command = self.perform_loging)
      loging_but.pack(pady=(10,10))

      lable3 = Label(self.root, text='Not a member ?')
      lable3.pack(pady=(20, 10))

      redirect_but = Button(self.root, text='Register now',command=self.register_gui)
      redirect_but.pack(pady=(10, 10))


   def register_gui(self):
      self.clear()


      heading = Label(self.root, text='NLPApp', bg='#a93226', fg='white')
      heading.pack(pady=(30, 30))
      heading.config(font=('verdana', 24, 'bold'))

      lable0 = Label(self.root, text='Enter Name')
      lable0.pack(pady=(10, 10))

      self.name_input = Entry(self.root, width=30)
      self.name_input.pack(pady=(5, 10), ipady=4)



      lable1 = Label(self.root, text='Enter Email')
      lable1.pack(pady=(10, 10))

      self.email_input = Entry(self.root, width=30)
      self.email_input.pack(pady=(5, 10), ipady=4)

      lable2 = Label(self.root, text='Enter password')
      lable2.pack(pady=(10, 10))

      self.password_input = Entry(self.root, width=30, show='*')
      self.password_input.pack(pady=(5, 10), ipady=4)

      register_but = Button(self.root, text='Register', width=30, height=2,command=self.perform_registration)
      register_but.pack(pady=(10, 10))

      lable3 = Label(self.root, text='All ready a member ?')
      lable3.pack(pady=(20, 10))

      redirect_but = Button(self.root, text='Login now', command=self.loging_gui)
      redirect_but.pack(pady=(10, 10))
   def clear(self):
       for i in self.root.pack_slaves():
           i.destroy()

   def perform_registration(self):
       name=self.name_input.get()
       email=self.email_input.get()
       password=self.password_input.get()

       responce=self.dbo.add_data(name,email,password)

       if responce:
           messagebox.showinfo('succes','Registration successfuly you can loging now')
           self.home_gui()

       else:
           messagebox.showerror('Error','Email already exite')


   def perform_loging(self):
       email=self.email_input.get()
       password=self.password_input.get()

       responce=self.dbo.search(email,password)

       if responce:
           messagebox.showinfo('succes','Login successfuly ')
           self.home_gui()
       else:
           messagebox.showerror('Error','Incorrect Email/password')

   def home_gui(self):

       self.clear()

       heading = Label(self.root, text='NLPApp', bg='#a93226', fg='white')
       heading.pack(pady=(30, 30))
       heading.config(font=('verdana', 24, 'bold'))

       sentiment_but = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
       sentiment_but.pack(pady=(10, 10))

       ner_but = Button(self.root, text='Named enatity recognition', width=30, height=4,
                              command=self.perform_registration)
       ner_but.pack(pady=(10, 10))

       Emotion_but = Button(self.root, text='Emotion prediction', width=30, height=4,
                              command=self.perform_registration)
       Emotion_but.pack(pady=(10, 10))

       logout_but = Button(self.root, text='Logout', command=self.loging_gui)
       logout_but.pack(pady=(10, 10))

   def sentiment_gui(self):

       self.clear()

       heading = Label(self.root, text='NLPApp', bg='#a93226', fg='white')
       heading.pack(pady=(30, 30))
       heading.config(font=('verdana', 24, 'bold'))

       heading = Label(self.root, text='Sentiment Analysis', bg='#a93226', fg='white')
       heading.pack(pady=(10, 20))
       heading.config(font=('verdana', 20))

       lable1 = Label(self.root, text='Enter a text')
       lable1.pack(pady=(10, 10))

       self.sentiment_input = Entry(self.root, width=30, show='*')
       self.sentiment_input.pack(pady=(5, 10), ipady=4)

       redirect_but = Button(self.root, text='Analyze sentiment', )
       redirect_but.pack(pady=(10, 10))

       self.sentiment_result = Label(self.root, text='' , bg='#a93226', fg='white')
       self.sentiment_result.pack(pady=(10, 10))
       self.sentiment_result.config(font=('verdana', 16))

       Goback_but = Button(self.root, text='Go Back', command=self.home_gui)
       Goback_but.pack(pady=(10, 10))

   def do_sentimentanalysis(self):
       pass



nlp=NLPAPP()




