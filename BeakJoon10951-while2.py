while True:
    try:
        a , b = map(int, input().split())
    except:
        break
    else:
        print(a+b)
