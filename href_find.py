import requests
import re

req = requests.get('http://pastebin.com/raw/hfMThaGb')
text = str(req.content)

lst = re.findall(r'<a.*?(?:href=").*?"', text)
s = set()
for i in lst:
    print(i)
    r = re.search(r'([0-9a-z]([0-9a-z\-])*[0-9a-z]\.)+[a-z]{2,4}', i)
    if r:
        s.add(r[0])

print(*sorted(s), sep='\n')
