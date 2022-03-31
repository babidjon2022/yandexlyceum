import datetime


class Date:

    def __init__(self, month, day):
        self.date = datetime.datetime(year=datetime.datetime.now().year,
                                      month=month,
                                      day=day)

    def __sub__(self, cl2):
        return (self.date - cl2.date).days
