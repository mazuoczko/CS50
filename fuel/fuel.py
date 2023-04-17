
while True:
    x = input('Fraction: ')
    if  '/' not in x:
        continue
    else:
        try:
            a,b =x.split('/')
            c = int(a)/int(b)
            d = c * 100
            g = round(d)
            g = int(g)

            if g > 100:
                continue
            elif g <= 1:
                print('E')
            elif g >= 99:
                print('F')
            else:
                print(g,'%',sep='')
        except (ValueError, ZeroDivisionError):
            continue
        else:
            break
