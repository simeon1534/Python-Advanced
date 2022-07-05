def age_assignment(*args, **kwargs):
    dictionary = {}
    for el in args:
        dictionary[el] = 0
    for key, value in kwargs.items():
        for el in dictionary.keys():
            if el[0] == key:
                dictionary[el]=value
    return dictionary


print(age_assignment("Peter", "George", G=26, P=19))  # {'Peter': 19, 'George': 26}
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))