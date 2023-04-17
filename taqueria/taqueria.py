dic = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
c = 0

while True:

    try:
        a = input('Item: ').title()
        b = dic.get(a)
        e = float(b)
        c = c + e
        print(f"Total: ${c:.2f}")
        continue
    except EOFError:
        break
    except ValueError:
        continue
    except TypeError:
        continue


