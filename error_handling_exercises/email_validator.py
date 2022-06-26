import re

command = input()


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while command != "End":
    email = command
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    name = re.split("@", email)[0]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    mail_domain = re.split("@", email)[1]
    domain = re.split("\.", mail_domain)[1]
    if domain not in ['com', 'bg', 'org', 'net']:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print('Email is valid')
    command = input()
