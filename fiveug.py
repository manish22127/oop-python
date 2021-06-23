class std:
    def __init__(self,usn=None,name=None,age=None):
        self.usn=usn
        self.name=name
        self.age=age
    def getdata(self):
        self.usn=input("enter the usn")
        self.name=input("enter the name")
        self.age=int(input("enter the age"))
    def display(self):
        print("usn : ",self.usn)
        print("name : ",self.name)
        print("age :",self.age)
class UGstudent(std):
        def __init__(self,sem=None,fees=None,stifend=None):
            self.sem=sem
            self.fees=fees
            self.stifend=stifend
        def UGdata(self):
            self.getdata()
            self.sem=input("entere the semister")
            self.fees=int(input("entere the fee"))
            self.stifend=int(input("entere the stifend"))
        def UGdisplay(self):
            self.display()
            print("smester is  :",self.sem)
            print("semester fee is :",self.fees)
            print("stipend fee is :",self.stifend)
class PGstudent(std):
    def __init__(self,sem=None,fees=None,stipend=None):
        self.sem=sem
        self.fees=fees
        self.stipend=stipend
    def PGdata(self):
        self.getdata()
        self.sem=input("enter the semester")
        self.fees=int(input("ente the fees"))
        self.stipend=int(input("enter the stifend"))
    def PGdisplay(self):
        self.display()
        print("semester is :",self.sem)
        print("semester fee is :",self.fees)
        print("stipend fee is :",self.stipend)
while True:
        print("*"*70)
        print("1. enter the UGdata")
        print("2. enter the PGdata")
        print("3.display UGdata")
        print("4.display PGdata")
        print("5.exit")
        ch=int(input("enter the choice"))
        if ch==1:
            print("enter the UGdata")
            s1=UGstudent()
            s1.UGdata()
        elif ch==2:
            print("enter the PGdata")
            s2=PGstudent()
            s2.PGdata()
        elif ch==3:
            print("display UGdata")
            s1.UGdisplay()
        elif ch==4:
            print("display PGdata")
            s2.PGdisplay()
        elif ch==5:
            break
        else:
            print("invalid input")










