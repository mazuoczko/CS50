import emoji

def emojizee():
    slowo = input()

    x = slowo.replace(":)", ":slightly_smiling_face:")
    i = x.replace(":(", ":slightly_frowning_face:")

    j = emoji.emojize(i)


    print(j)


def main():
    emojizee()

if __name__ == "__main__":
    main()
