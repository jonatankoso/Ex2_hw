class Date(object):
    def __init__(self, date):
        self.day, self.month, self.year = int(date.split("."))

    def set_day(self, new_day: str):
        self.day = new_day

    def set_month(self, new_month: str):
        self.month = new_month

    def set_year(self, new_year: str):
        self.year = new_year

    def fix_date(self, day, month, year):
        if day > 31:
            month += 1
            day -= 31
        if month > 12:
            year += 1
            month -= 12

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __add__(self, other):
        new_year = self.year + other.year
        new_month = self.month + other.month
        new_day = self.day + other.day

        # Adjust the date components if they exceed their respective limits
        if new_day > 31:
            new_month += 1
            new_day -= 31
        if new_month > 12:
            new_year += 1
            new_month -= 12

        return Date(new_year, new_month, new_day)