#!/usr/bin/env python3
import random

symbols = ['+', '-', '']
src = []

for i in range(9, -1, -1):
    src.append(str(i))
    if i == 0: break
    src.append('')


res_set = set()
for i in range(20):    
    res = 0
    while res != 200: 
        for j in range(1, 19, 2):
            src[j] = random.choice(symbols)
        code = ''.join(src)
        res = eval(code)
    res_set.add(code)

print('\n'.join(res_set))
