while True:
    try:
        N = int(input())
        matriz = []
        contador = N -1
        for linha in range(N):
            lista = []
            for coluna in range(N):
                if coluna == contador:
                    lista.append(2)
                    contador -= 1
                else:
                    if linha == coluna:
                        lista.append(1)
                    else:
                        lista.append(3)
            matriz.append(lista)
        for linha in range(N):
            for coluna in range(N):
                print(f"{matriz[linha][coluna]}", end = '')
            print()

                    
             
    except:
        break;
