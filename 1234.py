while True:
    try:
        texto = input()
        saida = ""
        M = True
        for saida2 in texto:
            if(saida2 == " "):
                saida += saida2
            elif(M):
                saida += saida2.upper()
                M = False
            else:
                saida += saida2.lower()
                M = True
        print(saida)
    
    
    
    except:
        break;
