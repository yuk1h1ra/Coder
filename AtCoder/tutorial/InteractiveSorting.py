# -*- coding: utf-8 -*-
N, Q = map(int, input().split())

s = ''
for i in range(N):
    s += chr(65 + i)

for i in range(N):
    for j in range(N-1):
        print("? ", s[j], " ", s[j+1])

        ans = input()
        if ans == '>':
            s[j], s[j+1] = s[j+1], s[j]

print("! ", str(s))

