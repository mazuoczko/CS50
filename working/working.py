import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    k = re.search(r"^([1-9][0-2]*):*([0-9][0-9])* (AM|PM) to ([1-9][0-2]*):*([0-9][0-9])* (AM|PM)$", s)

    if k == None:
        raise ValueError


    if int(k.group(1)) > 12 or int(k.group(4)) > 12:
        raise ValueError


    if (k.group(4) == "AM" or "PM" )and (k.group =="AM"or"PM"):
        sh = newtime(k.group(3),k.group(1),k.group(2))
        eh = newtime(k.group(6),k.group(4),k.group(5))
        return (f"{sh} to {eh}")

    else:
        raise ValueError

def newtime(am_pm, houers, minuts):
    if am_pm == "AM":
        if int(houers) == 12:
            newh = "00"
        else:
            newh = houers

    elif am_pm == "PM":
        if int(houers) == 12:
            newh = "12"
        else:
            newh = int(houers) + 12



    if minuts == None:
        newm = "00"
        newt = f"{newh:>02}" + ":" + str(newm)

    elif int(minuts) >= 60:
        raise ValueError

    else:
        newm = minuts
        newt = f"{newh:>02}" + ":" + str(newm)

    return newt


if __name__ == "__main__":
    main()