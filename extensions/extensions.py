a = input("Fille name: ")
b = a.strip().lower()
if b.endswith(".gif"):
    print("image/gif")
elif b.endswith(".jpg"):
    print("image/jpeg")
elif b.endswith(".jpeg"):
    print("image/jpeg")
elif b.endswith(".png"):
    print("image/png")
elif b.endswith(".pdf"):
    print("application/pdf")
elif b.endswith(".txt"):
    print("text/plain")
elif b.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")