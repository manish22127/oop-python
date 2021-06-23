class std:
    def __init__(self,usn=None,name=None,age=None):
        self.usn=usn
        self.name=name
        self.age=age
    def get(self):
        self.usn=input("enter your usn")
        self.name=input("enter your name")
        self.age=input("enter your age")
    def display(self):
        print("usn is :",self.usn)
        print("name is :",self.name)
        print("age is :",self.age)
class sub(std):
    def __init__(self,sem=0,sub1=0,s2=0,s3=0,s4=0,s5=0):
        self.sem=sem
        self.sub1=sub1
        self.s2=s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
    def getm(self):
        self.sem=input("enter the semester")
        self.sub1=int(input("enter the marks"))
        self.s2 = int(input("enter the marks"))
        self.s3 = int(input("enter the marks"))
        self.s4 = int(input("enter the marks"))
        self.s5= int(input("enter the marks"))
class result(sub):
    def display(self):
        self.total=self.sub1+self.s2+self.s3+self.s4+self.s5
        self.per=(self.total/500)*100
        print(self.total,"\n")
        print(self.per)
m1=result()
m1.get()
m1.getm()
m1.display()


