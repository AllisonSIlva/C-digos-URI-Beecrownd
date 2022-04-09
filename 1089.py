while True:
    try:
        N = int(input())
        if N == 0:
            break;
        H = input().split(" ")
        H = [int(x) for x in H]
        H.append(H[0])
        H.append(H[1])
        cont = 0
        for i in range(1, N+1):
            if H[i] < H[i-1] and H[i] < H[i+1]:
                cont += 1
            elif H[i] > H[i-1] and H[i] > H[i+1]:
                cont += 1
        print(cont)
        
        
    except:
        break;
