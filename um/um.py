import re
import sys


def main():
    print(count(input("Text: ")))



def count(s):
    a = 0
    k = re.findall(r"\b *um\b *", s, re.IGNORECASE)
    if k == None:
        return a

    for _ in k:

        a = a + 1

    return a


if __name__ == "__main__":
    main()