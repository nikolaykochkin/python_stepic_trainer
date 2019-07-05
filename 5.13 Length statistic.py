text = 'Beautiful is better than ugly. Explicit is better than implicit.'
lst = list(map(lambda x: len(x), text.split(' ')))
'''dic = {i: lst.count(i) for i in sorted(set(lst))}  # Через генератор словаря
for line in dic.items():
    print(line[0], line[1], sep=': ')
'''
lst.sort()
from itertools import groupby
for key, group in groupby(lst):
    print(key)

# Через каунтер
'''    
from collections import Counter
c = Counter(lst)  
for line in c.items():
    print(line[0], line[1], sep=': ')
'''

