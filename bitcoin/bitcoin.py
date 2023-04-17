import sys
import requests

# Imput - with comand steytment n
try:

    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    n = sys.argv[1]
    # conwert n to flowt
    n = float(n)
    a = r.json()
    fvalue = a['bpi']['USD']['rate_float']
    respond = fvalue * n
    print(f"${respond:,.4f}")
# conwrsion inposible = ERROR
except ValueError:
    print("Comand-line argument is not a number")
    sys.exit(1)
except IndexError:
    print("Missing comand-line argument")
    sys.exit(1)
except requests.RequestException:
    sys.exit(1)



# multiplesion n waliu by bitcoin price

# ERRORS
