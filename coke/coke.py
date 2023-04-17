

cost = 50

while cost > 0:
    print(f"Amount Due: {cost}")
    coins = int(input("Insert Coin: "))

    if coins == 25  :
        cost = cost - coins

    elif coins == 10 :
        cost = cost - coins

    elif coins == 5:
        cost = cost - coins


print(f"change Owned: {cost * -1}")
