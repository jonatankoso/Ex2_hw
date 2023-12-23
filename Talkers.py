class Person(object):
    def __init__(self, fname: str, lname: str, age: int):
        '''
        :param str fname: first name of person
        :param str lname: second name of person
        :param int age: age of person
        :return: none
        '''

        self.fname = fname
        if age <= 0:
            print("age cannot be negative or 0, age set to 1")
            self.age = 1
        else:
            self.age = age

        self.fname = fname
        self.lname = lname

    def set_fname(self, new_fname):
        '''
        :param new_fname: updated first name
        :return: none
        '''
        self.fname = new_fname

    def set_lname(self, new_lname):
        '''
        :param new_lname: updated last name
        :return: none
        '''
        self.lname = new_lname

    def set_age(self, new_age):
        '''
        :param new_age: updated age
        :return: none
        '''
        self.age = new_age


class Talker(Person):
    def __int__(self, fname: str, lname: str, age: int):
        '''
        :param str fname: first name of talker
        :param str lname: second name of talker
        :param int age: age of talker
        :return: none
        '''
        super.__init__(fname, lname, age)

    def talk(self, text: str):
        '''
        :param text: printed text
        :return: none
        '''
        print(text)


class HappyTalker(Talker):
    def __int__(self, fname: str, lname: str, age: int):
        '''
        :param str fname: first name of HappyTalker
        :param str lname: second name of HappyTalker
        :param int age: age of HappyTalker
        :return: none
        '''
        super.__init__(fname, lname, age)

    def talk(self, text: str):
        '''
        :param text: printed text
        :return: none
        '''
        print(text + "!!!")

class SlowTalker(Talker):
    def __int__(self, fname: str, lname: str, age: int):
        '''
        :param str fname: first name of SlowTalker
        :param str lname: second name of SlowTalker
        :param int age: age of SlowTalker
        :return: none
        '''
        super.__init__(fname, lname, age)

    def talk(self, text: str):
        '''
        :param text: printed text
        :return: none
        '''
        for letter in text:
            print(letter + " ", end="")

class StutterTalker(Talker):
    def __int__(self, fname: str, lname: str, age: int):
        '''
        :param str fname: first name of StutterTalker
        :param str lname: second name of StutterTalker
        :param int age: age of StutterTalker
        :return: none
        '''
        super.__init__(fname, lname, age)

    def talk(self, text: str):
        '''
        :param text: printed text
        :return: none
        '''
        words = text.split()
        result = ""
        for word in words:
            if len(word) > 0:
                result += word[0] * 3 + word[1:] + " "

        print(result)


def makeThemTalk(talkerList, sayWhat):
    '''
    :param list talkerList: list of people
    :param str sayWhat: text for the people in list to say
    :return: none
    '''
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
