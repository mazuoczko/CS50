import sys
from PIL import Image, ImageOps


n = sys.argv
k = len(sys.argv)
l = [".jpg", ".jpeg", ".png"]



if k < 3:
    print("Too few comand-line arguments")
    sys.exit(1)

if k > 3:
    print("Too many comand_line arguments")
    sys.exit(1)

if k == 3:
    try:
        for i in l:
            if n[1].endswith(i) and n[2].endswith(i):



                        b = sys.argv[2]
                        a = Image.open("shirt.png")
                        size = a.size
                        a = ImageOps.fit(a, size)
                        image = Image.open(sys.argv[1])
                        image = ImageOps.fit(image, size)
                        image.paste(a, a)
                        image.save(b)

                        sys.exit(0)

        else:
            print("Inwalid Input")
            sys.exit(1)



    except FileNotFoundError:
        sys.exit(1)
