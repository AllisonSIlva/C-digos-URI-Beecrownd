# -*- coding: utf-8 -*-
while True:
    try:
        A, B, C = input().split(" ")
        A = int(A)
        B = int(B)
        C = int(C)
        
        if (A == 0 and B == 0 and C == 0) or (A == 1 and B == 1 and C == 1):
            print("*")
        elif (A == 1 and B == 0 and C == 0) or (A == 0 and B == 1 and C == 1):
            print("A")
        elif (A == 0 and B == 1 and C == 0) or (A == 1 and B == 0 and C == 1):
            print("B")
        elif (A == 0 and B == 0 and C == 1) or (A == 1 and B == 1 and C == 0):
            print("C")
        
    except:
        break;
