shift = int(input())
text = input().strip()
alphabet = u' abcdefghijklmnopqrstuvwxyz'
shift_function = lambda x: alphabet[(alphabet.index(x) + shift) % len(alphabet)]
print('Result: "', *map(shift_function, text), '"', sep='')
