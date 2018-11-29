
GROWER = lambda x0, x1: x1 >= x0
SHRINKER = lambda x0, x1: x1 <= x0
    
def list_matches(iterable: list, func: "f(x, y)") -> bool:
    """ given an iterable 'iterable' and a function(x0, x1) 'func': will determine
        if func(iterable[i], iterable[i+1]) is true for len(iterable) > i > 0"""
    c = iterable[0]
    for i in range(1, len(iterable)):
        if not func(c, iterable[i]):
            # when a 'func' comparison fails, list_matches fails
            return False
        c = iterable[i]
    return True

def is_bouncy(iterable: list) -> bool:
    """ given an iterable of ints 'i' between 0 and 9, determines whether the int that i represents
        is bouncy."""
    return not (list_matches(iterable, GROWER)
            or (list_matches(iterable, SHRINKER)))

def int_to_iter(n: int) -> list:
    """ given an integer, creates a list of ints representing each didgit of the int in order"""
    assert isinstance(n, int)
    assert n >= 0
    iterable = []
    for char in str(n):
        iterable.append(int(char))
    return iterable


def main():
    bouncy = 0
    i = 99
    TARGET_PROPORTION = 0.99
    while bouncy/i != TARGET_PROPORTION:
        i += 1
        bouncy += (1 if is_bouncy(int_to_iter(i)) else 0) # adds 1 to bouncy when i is bouncy
    print(i, bouncy, bouncy/i)

if __name__ == "__main__":
    main()
