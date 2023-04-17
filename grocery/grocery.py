lis = {}

while True:
    try:
        a = input().upper()

        if a in lis:
            lis[a] += 1

        else:
            lis[a] = 1

    except EOFError:

        for j in sorted(lis.keys()):
            print(lis[j], j)

        else:
            break