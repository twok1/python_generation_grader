class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature
        
    def to_fahrenheit(self):
        return (self.temperature * 9 / 5) + 32
    
    @classmethod
    def from_fahrenheit(self, temperature):
        temperature = (5 / 9) * (temperature - 32) 
        return Temperature(temperature)
    
    def __str__(self) -> str:
        return f'{round(self.temperature, 2)}°C'
    
    def __bool__(self):
        return self.temperature > 0
    
    def __int__(self):
        return int(self.temperature)
    
    def __float__(self):
        return float(self.temperature)
    
    