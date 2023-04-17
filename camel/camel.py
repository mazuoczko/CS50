camel = input("camelCase: ")

a = camel.strip()

for i in a:
    if i == i.upper():
        a =  a.replace(i , f"_{i}")
        continue



d = a.lower()
print("snake_case: ",d )