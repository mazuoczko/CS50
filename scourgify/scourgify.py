import sys
import csv

n = len(sys.argv)
students = []
output = []

if n < 3:
    print("Too few comand-line arguments")
    sys.exit(1)

elif n > 3:
    print("Too many comand-line arguments")
    sys.exit(1)

elif n == 3:
    k = sys.argv
    try:
        if k[1].endswith(".csv") and k[2].endswith(".csv"):

            with open(k[1], "r") as file:
                reader = csv.DictReader(file)

                for line  in reader:
                    split_name = line["name"].split(",")
                    output.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": line["house"]})

            with open(k[2], "w") as doku:
                writer = csv.DictWriter(doku, fieldnames=["first","last","house"])
                writer.writerow({"first": "first", "last": "last", "house": "house"})
                for row in output:
                    writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

                sys.exit(0)


    except FileNotFoundError:
        print(f"Could not read {k[1]}")
        sys.exit(1)

    else:
            print("Not a Csv Fille")
            sys.exit(1)




