class Person(object):
    def __int__(self, fname, lname, age):
        if age <= 0:
            print("age cannot be negative or 0, age set to 1")
            self.age = 1
        else:
            self.age = age
        self.fname = fname
        self.lname = lname

    def set_fname(self, new_fname):
        self.fname = new_fname

    def set_lname(self, new_lname):
        self.lname = new_lname

    def set_age(self, new_age):
        self.age = new_age

class Talker(object):
    def __int__(self):