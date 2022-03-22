joias = []
while True:
    try:
        joias.append(input())        
    except:
        break;
joias = set(joias)
print(len(joias))
