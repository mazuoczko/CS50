import sys
import csv
from tabulate import tabulate

list = []

k = len(sys.argv)

try:

    if k > 2:
        print('Too many comand-line arguments')
        sys.exit(1)

    elif k < 2:
        print('Too few comand-line arguments')
        sys.exit(1)

    elif k == 2:
        n = sys.argv[1]

        if n.endswith('.csv') == False:
            print('Not a CSV fille')
            sys.exit(1)

        else:
            with open(n) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    list.append(row)

            print(tabulate(list[1:], headers=list[0], tablefmt="grid"))



except FileNotFoundError:
        print('Fille do not exsist')
        sys.exit(1)