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


class HappyTalker(Talker):
    def __int__(self, fname: str, lname: str, age: int):
        super.__init__(fname, lname, age)

    def talk(self, text: str):
        print(text + "!!!")

class SlowTalker(Talker):
    def __int__(self, fname: str, lname: str, age: int):
        super.__init__(fname, lname, age)

    def talk(self, text: str):
        for letter in text:
            print(letter + " ", end = "")

class StutterTalker(Talker):
    def __int__(self, fname: str, lname: str, age: int):
        super.__init__(fname, lname, age)

    def talk(self, text: str):
        words = text.split()
        result = ""
        for word in words:
            if len(word) > 0:
                result += word[0] * 3 + word[1:] + " "

        print(result)


def makeThemTalk(talkerList, sayWhat):
    for talker in talkerList:
        if talker.age > 10:
            print(talker.fname + ": ", end="")
            talker.talk(sayWhat)

if __name__ == "__main__":
    talkersList = []
    t1 = StutterTalker("may", "cohen", 19)
    t2 = HappyTalker("yan", "zikri", 23)
    t3 = SlowTalker("noam", "tzabari", 30)
    t4 = StutterTalker("noy", "furman", 9)

    talkersList.append(t1)
    talkersList.append(t2)
    talkersList.append(t3)
    talkersList.append(t4)
    makeThemTalk(talkersList, "How Are You?")
