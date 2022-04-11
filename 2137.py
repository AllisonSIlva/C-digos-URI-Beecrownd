while True:
    try:
        N = int(input())
        livros = []
        for i in range(N):
            i = int(input())        
            livros.append(i)
        livros.sort()
        for i in livros:
            print(f'{i:04}')
    except:
        break;
