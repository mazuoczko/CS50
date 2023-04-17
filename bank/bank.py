a = input("Greeting: ")
b = a.lower().strip()

if b.startswith("hello"):
    print("$0")

elif b.startswith("h"):
    print("$20")

else:
    print("$100")