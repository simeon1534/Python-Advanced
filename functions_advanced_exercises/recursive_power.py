def recursive_power(chislo, stepen):
    if stepen == 1:
        return chislo
    else:
        return chislo * recursive_power(chislo, stepen - 1)


print(recursive_power(2, 10))
