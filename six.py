class person:
    def hlo(self,name=None,age=None):
        self.name=name
        self.age=age
        if self.name != None and self.age != None:
            print("name AND AGE",(self.name,self.age))
        elif self.name != None :
            print("name ",(self.name))
        else :
            print("hlo")
p1=person()
p1.hlo()
p1.hlo("rvce")
p1.hlo("rvce",25)
