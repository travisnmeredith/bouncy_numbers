
GROWER = lambda x0, x1: x1 >= x0
SHRINKER = lambda x0, x1: x1 <= x0
SAMER = lambda x0, x1: x0 == x1
    
def list_matches(iterable, func):
    c = iterable[0]
    for i in range(1, len(iterable)):
        if not func(c, iterable[i]):
            return False
    return True



