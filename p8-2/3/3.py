from datetime import date, timedelta
from enum import Enum

class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class NextDate:
    def __init__(self, today: date, weekday: Weekday, considering_today=False):
        self.today = today
        self.weekday = weekday
        self.considering_today = considering_today
        self._days_until = 0

    def date(self):
        if not self.considering_today:
            self.today += timedelta(days=1)
            self._days_until += 1
        while self.today.weekday() != self.weekday.value:
            self.today += timedelta(days=1)
            self._days_until += 1
        return self.today

    def days_until(self):
        return self._days_until
    