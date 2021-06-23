class Employe:
    r_amt = 1.04
    def __init__(self,fname=0,lmane=0,cid=0,sal=0):
        self.fname=input("enter firsrt name")
        self.lname=input("enter the last name")
        self.cid=input("enter cid")
        self.sal=int(input("enter salary"))
    def display(self):
        print("first :",self.fname)
        print("lastname:", self.lname)
        print("Eid :",self.cid)
        print("salary :",self.sal)
    def raise_amt(self):
        self.final=self.sal*self.r_amt
        print("salary of EMPLOYEE after raise:",self.final)
class Manager(Employe):
    r_amt = 1.08
    def raise_amt(self):
        self.final=self.sal*self.r_amt
        print("salary of Manager after raise:",self.final)
class Director(Employe):
    r_amt = 1.01
    def raise_amt(self):
        self.final=self.sal*self.r_amt
        print("salary of director ofter raise",self.final)
e=Employe()
e1=Manager()
e2=Director()
e.display()
e.raise_amt()
e1.display()
e1.raise_amt()
e2.display()
e2.raise_amt()

