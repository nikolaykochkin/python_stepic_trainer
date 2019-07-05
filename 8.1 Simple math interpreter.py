operators = {'plus': (lambda x, y: x + y),
             'minus': (lambda x, y: x - y),
             'multiply': (lambda x, y: x * y),
             'divide': (lambda x, y: x // y)}
a, operator, b = input().split()
print(operators[operator](int(a), int(b)))
