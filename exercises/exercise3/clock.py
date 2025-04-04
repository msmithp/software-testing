class Clock():
    """ 24-hour clock, with times from 0:00 to 23:59"""
    def __init__(self, hrs, mins):
        self.hrs = hrs
        self.mins = mins
        self.format_time()

#Ensures that the time is in the correct 24 hour format and range
    def format_time(self):
        self.hrs += self.mins // 60
        self.mins = self.mins % 60
        self.hrs = self.hrs % 24

    def add_time(self, hrs, mins):
        self.hrs = hrs
        self.mins = mins
        self.format_time()

    def __str__(self):
        return f"{self.hrs:02d}:{self.mins:02d}"

    def __eq__(self, other):
        return self.hrs == other.hrs and self.mins == other.mins