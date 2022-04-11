while True:
    try:
        N = int(input())
        comportadas = 0
        Ncomportadas = 0
        lista = []
        for i in range(N):
            i, n = input().split(" ")
            i = str(i)
            n = str(n)
            if i == '+':
                comportadas += 1
            elif i == '-':
                Ncomportadas += 1
            lista.append(n)
        lista.sort()
        for i in lista:
            print(i)
        print("Se comportaram:", comportadas,"| Nao se comportaram:", Ncomportadas)
    except:
        break;
