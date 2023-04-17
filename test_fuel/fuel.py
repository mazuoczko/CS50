def main():

    fraction = input('Fraction: ')
    g = convert(fraction)
    p = gauge(g)
    print(p)


def convert(fraction):

        if  '/' not in str(fraction):
                return False
        else:
            try:
                a,b = fraction.split('/')
                c = int(a)/int(b)
                d = c * 100
                g = round(d)
                g = int(g)
                return(g)

            except ZeroDivisionError:
                return ZeroDivisionError
            except ValueError:
                return ValueError


def gauge(percentage):

        if percentage > 100:
            return ValueError

        elif percentage <= 1:
            return('E')

        elif percentage >= 99:
            return('F')

        else:
            return(f'{percentage}%')


if __name__ == "__main__":
    main()