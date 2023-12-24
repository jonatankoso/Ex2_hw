class Person(object):
    def __init__(self, fname: str, lname: str, age: str):
        '''
        :param str fname: first name of person
        :param str lname: second name of person
        :param int age: age of person
        :return: none
        '''
        if not str(age).isnumeric():
            print("age cannot be negative or 0 or a string")
            raise ValueError()
        else:
            self.age = int(age)

        if not fname.isalpha():
            print("first name needs to include only letters")
            raise TypeError()
        else:
            self.fname = fname

        if not lname.isalpha():
            print("last name needs to include only letters")
            raise TypeError()
        else:
            self.lname = lname

    def set_fname(self, new_fname):
        '''
        function updates first name of person
        :param new_fname: updated first name
        :return: none
        '''
        if not new_fname.isalpha():
            print("last name needs to include only letters")
            raise TypeError()
        else:
            self.fname = new_fname

    def set_lname(self, new_lname):
        '''
        function updates last name of person
        :param new_lname: updated last name
        :return: none
        '''
        if not new_lname.isalpha():
            print("last name needs to include only letters")
            raise TypeError()
        else:
            self.lname = new_lname

    def set_age(self, new_age):
        '''
        function updates age of person
        :param new_age: updated age
        :return: none
        '''
        if not str(new_age).isnumeric():
            print("age cannot be negative or 0 or a string")
            raise ValueError()
        else:
            self.age = int(new_age)


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
        function prints given string
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
        function prints given string
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
        function prints given string
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
        function prints given string
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
    function prints given text based on speech of people in list
    :param list talkerList: list of people
    :param str sayWhat: text for the people in list to say
    :return: none
    '''
    for talker in talkerList:
        if talker.age > 10:
            print(talker.fname + ": ", end="")
            talker.talk(sayWhat)

if __name__ == "__main__":
    try:
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
    except TypeError:
        print("Wrong type of operands")
    except ValueError:
        print("Wrong value of operands, check input")

