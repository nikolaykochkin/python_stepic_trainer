in_lst = [int(i) for i in input().split(' ')]
abs_dif_lst = sorted([abs(in_lst[x]-in_lst[x-1]) for x in range(1, len(in_lst))])

if abs_dif_lst == list(range(1, len(in_lst))):
    print('Jolly')
else:
    print('Not jolly')
