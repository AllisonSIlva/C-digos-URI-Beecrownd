while True:
    try:
        N = int(input())
        if N == 0:
            break;
        V = input().split(" ")
        Z = sorted(V, key = int)
        for i, x in enumerate(V):
            if x == Z[N-2]:
                print(i + 1)
    except:
        break;
