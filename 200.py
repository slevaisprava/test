#!/usr/bin/env python3
import random

symbols = ['+', '-', '']

i = 9
src = []
while i >= 0:
    src.append(str(i))
    if i == 0: break
    src.append('')
    i -= 1

res_set = set()
for i in range(20):    
    res = 0
    while res != 200: 
        for i in range(1, 19, 2):
            src[i] = random.choice(symbols)
            code = ''.join(src)
            res = eval(code)
    res_set.add(str(code))
    i += 1

print('\n'.join(res_set))
