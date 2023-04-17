import validators

e = input("What's your email addres? ")

if validators.email(e):
    print("Valid")

else:
    print("Invalid")