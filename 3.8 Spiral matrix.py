n = int(input())
lst = [[0 for i in range(n)] for i in range(n)]
i = j = di = 0
dj = cnt = 1
max = n - 1
while cnt <= n ** 2:
    for y in range(4):
        for z in range(max):
            lst[i][j] = str(cnt)
            cnt += 1
            i += di
            j += dj

        if dj == 1:
            di, dj = 1, 0
        elif di == 1:
            di, dj = 0, -1
        elif dj == -1:
            di, dj = -1, 0
            max -= 1
        else:
            di, dj = 0, 1
    lst[i][j] = str(cnt)
    j += 1
    cnt += 1
    max -= 1

for i in range(n):
    print('\t'.join(lst[i]))