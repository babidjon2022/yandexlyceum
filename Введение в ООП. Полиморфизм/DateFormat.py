import datetime as dt


class AmericanDate:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, new_year):
        self.year = new_year

    def set_month(self, new_month):
        self.month = new_month

    def set_day(self, new_day):
        self.day = new_day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        date = dt.date(year=self.year, month=self.month, day=self.day)
        return date.strftime('%m.%d.%Y')


class EuropeanDate:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, new_year):
        self.year = new_year

    def set_month(self, new_month):
        self.month = new_month

    def set_day(self, new_day):
        self.day = new_day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        date = dt.date(year=self.year, month=self.month, day=self.day)
        return date.strftime('%d.%m.%Y')
