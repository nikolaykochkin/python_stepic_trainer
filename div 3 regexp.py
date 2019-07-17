import re

#text = input()
text = '''0
10010
00101
01001
Not a number
1 1
0 0'''

for i in text.split('\n'):
    if re.search(r'(?:0|1(?:01*0)*1)*', i)[0] == i:
        print(i)
