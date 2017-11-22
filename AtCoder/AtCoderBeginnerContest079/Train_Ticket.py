# -*- coding: utf-8 -*-

N = input()
A, B, C, D = int(N[0]), int(N[1]), int(N[2]), int(N[3])

if A+B+C+D==7:
    print("{}+{}+{}+{}=7".format(A, B, C, D)) 
elif A+B+C-D==7:
    print("{}+{}+{}-{}=7".format(A, B, C, D)) 
elif A+B-C+D==7:
    print("{}+{}-{}+{}=7".format(A, B, C, D)) 
elif A+B-C-D==7:
    print("{}+{}-{}-{}=7".format(A, B, C, D)) 
elif A-B+C+D==7:
    print("{}-{}+{}+{}=7".format(A, B, C, D)) 
elif A-B+C-D==7:
    print("{}-{}+{}-{}=7".format(A, B, C, D)) 
elif A-B-C+D==7:
    print("{}-{}-{}+{}=7".format(A, B, C, D)) 
elif A-B-C-D==7:
    print("{}-{}-{}-{}=7".format(A, B, C, D)) 
