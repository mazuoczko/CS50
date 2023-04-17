from twttr import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten('anastazja') == 'nstzj'
    assert shorten('ambrozja') == 'mbrzj'
    assert shorten('AMBROZJA') == 'MBRZJ'

def test_numbers():
    assert shorten('1234') == '1234'

def test_pun():
    assert shorten('?!.,') == '?!.,'


if __name__ == "__main__":
    main()