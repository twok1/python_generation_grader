import re

class DomainException(Exception):
    pass

def check_domain(domain):
    return re.match(r'^[A-Za-z]+\.[A-Za-z]+$', domain)

def check_url(url):
    return re.match(r'http[s]{0,1}://[A-Za-z]+\.[A-Za-z]+', url)

def check_email(email):
    return re.match(r'[A-Za-z]+@[A-Za-z]+\.[A-Za-z]+', email)

class Domain:
    def __init__(self, domain):
        if not check_domain(domain):
            raise DomainException('Недопустимый домен, url или email')
        self.domain = domain

    @classmethod
    def from_url(cls, url):
        if not check_url(url):
            raise DomainException('Недопустимый домен, url или email')
        return cls(url[url.find('//')+2:])

    @classmethod
    def from_email(cls, email):
        if not check_email(email):
            raise DomainException('Недопустимый домен, url или email')
        return cls(email[email.find('@')+1:])
    
    def __str__(self):
        return self.domain

