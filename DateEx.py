from datetime import datetime, timedelta

class Date(object):
    def __init__(self, date: str):
        '''
        function initializes fields of date class
        :param date: date input from user
        '''
        self.day, self.month, self.year = date.split(".")
        if not str(self.day).isnumeric() or not str(self.month).isnumeric() or not str(self.year).isnumeric():
            print("date is negative or not in correct format of date: dd.mm.yy")
            raise ValueError()
        if self.year < "1990":
            self.set_year(self.year)

    def set_day(self, new_day: str):
        '''
        function updates the day of the date
        :param new_day: updated day
        :return: none
        '''
        self.day = new_day

    def set_month(self, new_month: str):
        '''
        function updates the month of the date
        :param new_month: updated month
        :return: none
        '''
        self.month = new_month

    def set_year(self, new_year: str):
        '''
        function updates the year of the date
        :param new_year: updates year
        :return: none
        '''
        self.year = new_year

    def __str__(self):
        '''
        function prints the date
        :return: date in str format dd.mm.yyyy
        '''
        return f"{self.day}.{self.month}.{self.year}"

    def __add__(self, other):
        '''
        funtion adds 2 dates
        :param other: other date to be added
        :return: sum of 2 dates
        '''
        selfDateFormat = datetime(int(self.year), int(self.month), int(self.day))
        if isinstance(other, int):
            formatted_date = (selfDateFormat + timedelta(days=other))
            formatted_year = formatted_date.year % 100
            formatted_date = formatted_date.strftime('%d.%m')
            if formatted_year < 10:
                formatted_year = "0" + str(formatted_year)
            return str(formatted_date) + "." + str(formatted_year)

        elif isinstance(other, Date):
            otherDateFormat = datetime(int(other.year), int(other.month), int(other.day))
            difference = otherDateFormat - datetime.min
            formatted_date = (selfDateFormat + difference)
            formatted_year = formatted_date.year % 100
            formatted_date = formatted_date.strftime('%d.%m')
            return str(formatted_date) + "." + str(formatted_year)

        else:
            raise TypeError("Unsupported operand type. Expected an integer or Date object.")

    def __sub__(self, other):
        '''
        function subtracts 2 dates from one another
        :param other: date to be subtracted from self
        :return: the number of days between the two dates
        '''
        selfDateFormat = datetime(int(self.year), int(self.month), int(self.day))
        otherDateFormat = datetime(int(other.year), int(other.month), int(other.day))
        return (selfDateFormat - otherDateFormat).days

    def __eq__(self, other):
        '''
        function checks if 2 dates are equal
        :param other: other date to be checked
        :return: True if the dates are the same, else False
        '''
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __gt__(self, other):
        '''
        function  checks if the first date is equal or ahead of the second
        :param other: 2nd date to be compared
        :return: True if the first date is ahead or equal to the second, False otherwise
        '''
        return (self - other) > 0

    def __ge__(self, other):
        '''
        function  checks if the first date is ahead of the second
        :param other: 2nd date to be compared
        :return: True if the first date is ahead to the second, False otherwise
        '''
        return (self > other) or (self == other)

    def __lt__(self, other):
        '''
        function checks if the first date is before of the second
        :param other: 2nd date to be compared
        :return: True if the first date is before the second, False otherwise
        '''
        return (self - other) < 0

    def __le__(self, other):
        '''
        function checks if the first date is before or equal to the second
        :param other: 2nd date to be compared
        :return: True if the first date is before or equal to the second, False otherwise
        '''
        return (self < other) or (self == other)


if __name__ == "__main__":
    try:
        d1 = Date("01.09.05")
        d2 = Date("26.09.05")
        d1.set_year("06")
        print(d1)
        print(d1 + d2)
        print(d1 + 50000)
        print(d1 - d2)
        print(d1 == d2)
        print(d1 >= d2)
        print(d1 > d2)
        print(d1 >= d2)
        print(d1 < d2)
        print(d1 <= d2)
    except TypeError:
        print("Enter parameters of correct type")
    except ValueError:
        print("Enter legal date in range")