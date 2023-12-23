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

