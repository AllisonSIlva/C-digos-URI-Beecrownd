while True:
    try:
       N, K = input().split()
       N = int(N)
       K = int(K)
       chamada = []
       for i in range(N):
           i = input()
           chamada.append(i)
           chamada.sort()
       print(chamada[K-1])
       
    except:
        break;        
