# -*- coding: utf-8 -*-

N = int(input())

F = []
F.append(2)
F.append(1)

if N >= 2:
    for i in range(2, N + 1):
        F.append(F[i - 1] + F[i - 2])
    print(F[N])
else:
    print(F[N])
