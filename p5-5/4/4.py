class Time:
    def __init__(self, hours, minutes):
        self.minutes = minutes % 60
        self.hours = (hours + minutes // 60) % 24
        
    def __str__(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}"
    
    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours += other.hours
            self.minutes += other.minutes
            while self.minutes >= 60:
                self.minutes %= 60
                self.hours += 1
            self.hours %= 24
            return self
        return NotImplemented
    
# t = Time(22, 0)
# t += Time(3, 0)
# print(t)

# time1 = Time(2, 30)
# time2 = Time(3, 10)

# print(time1 + time2)
# print(time2 + time1)