class Person:
    def set_info(self, pid, pname, page): #self is used to refer to current object
        self.pid = pid
        self.pname = pname
        self.page = page

person1 = Person()   #object
person1.set_info(1233, "rutuja shinde", 30)
print(person1.pid, " : ", person1.pname, " : ", person1.page)
