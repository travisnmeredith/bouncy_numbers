
    
def list_matches(iterable, func):
    c = iterable[0]
    for i in range(1, len(iterable)):
        if not func(c, iterable[i]):
            return False
    return True

