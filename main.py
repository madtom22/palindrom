def palindrom (word:str):
    a = word.lower()
    b = (word[::-1].lower())
    if a==b:
        return True
    else:
        return False

print('Program sprawdzi czy podane przez Ciebie słowo jest palindromem - niezależnie od wielkości wpisanych liter.')
c = str(input('Podaj słowo: '))
print(palindrom(c))