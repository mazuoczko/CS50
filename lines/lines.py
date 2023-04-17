import sys

i = 0

#Pobieranie plikuz argumentu
k = len(sys.argv)

# czy się kończy na .py
if k > 2:
    print('To many comand-line arguments')
    sys.exit(1)

if k<2:
    print('Too few comand-line arguments')
    sys.exit(1)
if k == 2 :
    try:

        n = sys.argv[1]
        k = []

        if n.endswith('.py'):

            with open(n) as file:
            #lupa liczonca linie kodu

                for line in file:
                    if line.lstrip().startswith('#'):
                        pass
                    elif line.isspace():
                        pass
                    else:
                        i += 1

            print(f'{i}')

        else:
            print('Not a phyton fille')
            sys.exit(1)



    except FileNotFoundError:
            sys.exit(1)


