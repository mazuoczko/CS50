import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))



def validate(ip):

    if port := re.search("^([1-2]?[0-5]?[0-9]).([1-2]?[0-5]?[0-9]).([1-2]?[0-5]?[0-9]).([1-2]?[0-5]?[0-9])$",ip):


        if int(port.group(1)) > 255 or int(port.group(2)) > 255 or int(port.group(3)) > 255 or int(port.group(4)) > 255:
            return False


        else:
            return True


    else:
        return False



if __name__ == "__main__":
    main()