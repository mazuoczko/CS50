def main():
    slowo = input()
    print(shorten(slowo))



def shorten(word):

    g = str(word)

    while 1 == 1:
        g = g.replace('a',"")
        g = g.replace('e',"")
        g = g.replace('i',"")
        g = g.replace('o',"")
        g = g.replace('u',"")
        g = g.replace('A',"")
        g = g.replace('E',"")
        g = g.replace('I',"")
        g = g.replace('O',"")
        g = g.replace('U',"")
        return(g)


if __name__ == "__main__":
    main()