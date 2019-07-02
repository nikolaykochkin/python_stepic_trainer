n = int(input())
lst = [[0] * n for i in range(n)]
i = j = di = 0
dj = cnt = 1

while cnt <= n ** 2:
    lst[i][j] = cnt
    if lst[(i + di) % n][(j + dj) % n]:
        di, dj = dj, -di
    i, j = i + di, j + dj
    cnt += 1

for l in lst:
    print(*l)
