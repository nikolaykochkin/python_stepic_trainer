def continued_fraction(a, b):
    q = []
    while b != 0:
        q.append(a // b)
        a, b = b, a % b
    return q


lst = list(map(lambda x: int(x), input().split('/')))
print(*continued_fraction(lst[0], lst[1]))
