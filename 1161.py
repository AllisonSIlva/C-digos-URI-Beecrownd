while True:
    try:
        M, N = input().split(" ")
        M = int(M)
        N = int(N)
        iN = N
        iM = M
        fatM = 1 
        fatN = 1
        while iM > 0:
            fatM *= iM
            iM -= 1
        while iN > 0:
            fatN *= iN
            iN -= 1
        print(fatM + fatN)
    except:
        break;
