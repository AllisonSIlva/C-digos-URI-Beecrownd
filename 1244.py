N = int(input())
while N > 0:
    N -= 1
    x = input().split()
    x.sort(key=len, reverse=True)
    for i in range(len(x)):
        print(x[i], end='')
        if i != len(x)-1:
            print(' ', end='')
    print()
