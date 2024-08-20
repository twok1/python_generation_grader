from datetime import date

class DateFormatter:
    def __init__(self, country_code):
        self.country_code = country_code
        
    def __call__(self, d):
        if self.country_code in ('ru', 'fr'):
            f_str = '%d.%m.%Y'
        elif self.country_code == 'pt':
            f_str = '%d-%m-%Y'
        elif self.country_code == 'us':
            f_str = '%m-%d-%Y'
        elif self.country_code == 'ca':
            f_str = '%Y-%m-%d'
        elif self.country_code == 'br':
            f_str = '%d/%m/%Y'
        return date.strftime(d, f_str)