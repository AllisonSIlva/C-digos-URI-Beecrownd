while True:
    try:
        texto = input()
        vogais = ""
        for i in texto:
            if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
                vogais += i
        if(vogais[::-1] == vogais):
            print("S")
        else:
            print("N")
                
    except:
        break;
