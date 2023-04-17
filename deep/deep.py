a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
b = a.lower().strip()
if b == "42":
    print("Yes")
elif b == "forty two":
    print("Yes")
elif b == "forty-two":
    print("Yes")
else:
    print("NO")
    
