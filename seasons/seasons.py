from datetime import date
import re
import inflect
import sys




def main():

    time = input("Date of Birth: ")
    chec_forf(time)

def chec_forf(a):

    if d_o :=  re.search(r"^([1-2][0-9][0-9][0-9])-([0-1][0-9])-([0-3][0-9])$",a):
        to_day = date.today()
        last_day = date( int(d_o.group(1)), int(d_o.group(2)), int(d_o.group(3)))
        b = to_day - last_day
        k = b.days * 1440
        words = inflect.engine().number_to_words(k, andword="")
        print(words.capitalize() + " minutes")

    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()