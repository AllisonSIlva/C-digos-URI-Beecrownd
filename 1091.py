while True:
    try:
        K = int(input())
        N, M = input().split(" ")
        M = int(M)
        N = int(N)
        while K:
            K -= 1    
            X, Y = input().split(" ")
            X = int(X)
            Y = int(Y)
            
            if X == N or Y == M:
                print("divisa")
            
            elif X < N:
                if Y < M:
                    print("SO")
                elif Y > M:
                    print("NO")
                
            elif X  > N:
                if Y < M:
                    print("SE")
                elif Y > M:
                    print("NE")
    except:
        break;
