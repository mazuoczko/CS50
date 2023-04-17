import random


while True:
    try:
        r = input("Level: ")
        r = int(r) + 1
        lista = [*range(1, r, 1)]
        n = random.choice(lista)

    except ValueError:
        continue
    except IndexError:
        continue

    if int(r) <= 0:
        continue
    else:
        break


while True:

    try:
        m = input("Guess: ")
        if n < int(m):
            print("Too large!")
            continue
        elif n > int(m):
            print("Too small!")
            continue
        elif n == int(m):
            print("Just right!")
            break
        elif int(m) <= 0:
            continue


    except IndexError:
        continue
    except ValueError:
        continue

