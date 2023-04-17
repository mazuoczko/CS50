from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


if len(sys.argv) == 1:

    text= input('Input: ')
    m = random.choice(figlet.getFonts())
    figlet.setFont(font=m)
    print(figlet.renderText(text))

elif (len(sys.argv) == 3) and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in figlet.getFonts()):

    try:
        text= input('Input: ')
        f = sys.argv[2]
        figlet.setFont(font=f)
        print('Output: ', figlet.renderText(text))

    except :
        sys.exit(1)

else:
    sys.exit(1)


