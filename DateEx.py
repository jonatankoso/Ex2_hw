from datetime import datetime, timedelta

class Date(object):
    def __init__(self, date):
        self.day, self.month, self.year = date.split(".")

    def set_day(self, new_day: str):
        self.day = new_day

    def set_month(self, new_month: str):
        self.month = new_month

    def set_year(self, new_year: str):
        self.year = new_year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __add__(self, other):
        selfDateFormat = datetime(int(self.year), int(self.month), int(self.day))
        if isinstance(other, int):
            return (selfDateFormat + timedelta(days=other)).strftime('%d-%m-%Y')

        elif isinstance(other, Date):
            otherDateFormat = datetime(int(other.year), int(other.month), int(other.day))
            difference = otherDateFormat - datetime.min
            formatted_date = (selfDateFormat + difference).strftime('%d-%m-%Y')
            return formatted_date

        else:
            raise TypeError("Unsupported operand type. Expected an integer or Date object.")

    def __sub__(self, other):
        selfDateFormat = datetime(int(self.year), int(self.month), int(self.day))
        otherDateFormat = datetime(int(other.year), int(other.month), int(other.day))
        return (selfDateFormat - otherDateFormat).days



if __name__ == "__main__":
    date1 = Date("03.08.2005")
    date2 = Date("01.08.2005")
    print(date1 - date2)