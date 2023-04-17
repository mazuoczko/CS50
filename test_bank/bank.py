def main():

    greeting = input("Greeting: ")
    print(value(greeting))

def value(a):


    b = a.lower().strip()

    if b.startswith("hello"):
        return 0

    elif b.startswith("h"):
        return 20

    else:
        return 100

if __name__ == "__main__":
    main()