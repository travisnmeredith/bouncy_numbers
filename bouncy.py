
GROWER = lambda x0, x1: x1 >= x0
SHRINKER = lambda x0, x1: x1 <= x0
SAMER = lambda x0, x1: x0 == x1
    
def list_matches(iterable, func):
    c = iterable[0]
    for i in range(1, len(iterable)):
        if not func(c, iterable[i]):
            return False
        c = iterable[i]
    return True

def is_bouncy(iterable):
    return not (list_matches(iterable, GROWER)
            or (list_matches(iterable, SHRINKER))
            or (list_matches(iterable, SAMER)))

def int_to_iter(n):
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
        bouncy += (1 if is_bouncy(int_to_iter(i)) else 0)
    print(i, bouncy, bouncy/i)

if __name__ == "__main__":
    main()
