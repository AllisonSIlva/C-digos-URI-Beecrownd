while True:
    try:
        N = int(input())
        cont = 0
        for i in range(N):
            i = int(input())
            for j in range(1):
                j = input().split(" ")
                j = [int(i) for i in j]
                g = [int(i) for i in j]
                g.sort(reverse=True)
            for x in range(i):
                if g[x] == j[x]:
                    cont += 1
            print(cont)  
            cont = 0
    except:
        break;
