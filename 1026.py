while True:
    try:
        x, y = input().split(" ")
        x = int(x)
        y = int(y)
        print(int(x) ^ int(y))
    except:
        break;
