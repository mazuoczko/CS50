monts = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    # input MM-DD-YYYY
        date = input("Date:")
        try:
            m, d, y = date.strip().split("/")

            if (int(m) >=1 and int(m) <= 12) and (int(d)>= 1 and int(d)<=31):
                break
        except:
            try:
                om, od, y = date.split(" ")

                for i in range(len(monts)):
                    if om == monts[i]:
                        m = i + 1
                if not od.endswith(","):
                    continue
                d = od.replace(",","")

                if (int(m) >=1 and int(m) <= 12) and (int(d)>= 1 and int(d)<=31):
                    break
            except:
                print()
                pass

print(f"{y}-{int(m):02}-{int(d):02}")

        # chek if M is a int
        # transfer in to YYYY-MM-DD