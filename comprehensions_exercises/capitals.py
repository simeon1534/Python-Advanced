countries=tuple(input().split(', '))
capitals=tuple(input().split(', '))

zipped=zip(countries,capitals)

dictionary={country:capital for (country,capital) in zipped}
[print(f"{country} -> {capital}") for country,capital in dictionary.items()]

#print('\n'.join({f"{key} -> {value}" for (key,value) in zip(tuple(input().split(', ')),tuple(input().split(', ')))}))