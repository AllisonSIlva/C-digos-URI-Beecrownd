while True:
    try:
        texto = []
        texto = input().lower().split(" ")
        cont = 0
        cont2 = 0
        for i,j in enumerate(texto):
            texto[i] = j[0]
            if (texto[i] == texto[i - 1] and cont2 == 0):
                cont2 = 1
                cont += 1
            elif(texto[i] != texto[i - 1]):
                cont2 = 0
        print(cont)
        
                
    except:
        break;
