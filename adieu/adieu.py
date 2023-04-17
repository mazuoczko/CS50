import inflect
p = inflect.engine()
list =[]

while True:
    try:

        name = input("Name: ")
        list.append(name)

    except EOFError:

        break



list2 = p.join(list)
print("Adieu, adieu, to " + list2)
