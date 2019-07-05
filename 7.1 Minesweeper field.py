n, m = map(int, input().split(' '))
field = [[*input()] for i in range(n)]

for i in range(n):
    for j in range(m):
        if field[i][j] == '*':
            continue
        counter = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if ((i + di) in range(n)
                        and (j + dj) in range(m)
                        and field[i + di][j + dj] == '*'):
                    counter += 1
        field[i][j] = counter

for line in field:
    print(*line, sep='')
