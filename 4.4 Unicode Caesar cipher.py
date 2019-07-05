alphabet = ''.join([chr(i) for i in range(int(0x1f600), int(0x1f64f)+1)])

start, end = 0x1F600, 0x1F64F
chr( start + (ord(char) - start + offset) % (end - start + 1) )