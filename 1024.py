while True:
    try:
        N = int(input())
        for i in range(N):
            string = str(input())
            texto = []
            for letras in string:
                decoded = int(ord(letras))
                code = chr(decoded)
                if (code.isalpha()):
                    code = chr(decoded + 3)
                    texto.append(code)
                else:
                    texto.append(chr(decoded))
    
            texto = texto[::-1]
            texto = "".join(texto)
            lista2 = []
            for letras in texto[len(texto)//2:]:
                decoded = int(ord(letras))
                decoded = chr(decoded -1)
                lista2.append(decoded)
            txt2 = "".join(lista2)
            print(texto[:len(texto)//2] + txt2)                 
    except:
        break;
