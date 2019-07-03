from re import sub
name = sub(r'(^\s+|\s+$)', '', input())
print(sub(r'\s+', '_', name))
