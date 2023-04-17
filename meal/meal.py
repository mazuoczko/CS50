
def main():
    time = input("What time is it? ")
    a = convert(time)


    if a >= 7 and a <= 8:
        print("breakfast time")
    elif a >= 12 and a <= 13:
        print("lunch time")
    elif a >= 18 and a <= 19:
        print("dinner time")


def convert(time):
    hours , minutes = time.split(":")
    f1 = float(minutes)
    s1 = float(hours)
    zaokronglone = f1 /60
    a = s1 + zaokronglone

    return(a)



if __name__ == "__main__":
    main()