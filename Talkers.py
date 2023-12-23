class Person(object):
    def __init__(self, fname: str, lname: str, age: int):
        self.fname = fname
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


class Talker(Person):
    def __int__(self, fname: str, lname: str, age: int):
        super.__init__(fname, lname, age)

    def talk(self, text: str):
        print(text)


if __name__ == "__main__":
    t1 = Talker("may", "cohen", 19)
    t1.talk("hey")
