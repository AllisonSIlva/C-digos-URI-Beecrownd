while True:
    try:
        N = int(input())
        jogadas = input().split(" ")
        cont1 = 0
        cont2 = 0
        for x in jogadas:
            if x == '0':
                cont1 += 1
            else:
                cont2 += 1
        print("Mary won" , cont1 , "times and John won" , cont2 , "times")      
    
    
    
    
    except:
        break;
