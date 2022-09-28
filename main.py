def palindrom (word:str):
    a = word.lower()
    b = (word[::-1].lower())
    if a==b:
        return True
    else:
        return False