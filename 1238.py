while True:
    try:
        N = int(input())
        while N:
            N -= 1
            S1, S2 = input().split(" ")
            saida = ''
            x = 0
            while x < len(S1) and x < len(S2):
                saida += S1[x] + S2[x]
                x += 1
                
            if x <= len(S1):
                saida += S1[x:]
            if x <= len(S2):
                saida += S2[x:]
                
            print(saida)
    except:
        break;
