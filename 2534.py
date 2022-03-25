# -*- coding: utf-8 -*-
while True:
    try:
        N, Q = input().split(" ")
        N = int(N)
        Q = int(Q)
        lista = []
        
        while N:
            N -= 1
            nota = int(input())
            lista.append(nota)
        lista.sort(reverse = True)
        while Q:
            Q -= 1
            consulta = int(input())
            print(lista[consulta - 1])       
    except:
        break;
