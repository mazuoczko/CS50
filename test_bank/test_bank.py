from bank import value

def main():
    test_20()
    test_0()
    test_100()

def test_20():
    assert value('hi') == 20
    assert value('hiee') == 20
    assert value('Hiee') == 20


def test_0():
    assert value('hello') == 0
    assert value('Hello') == 0

def test_100():
    assert value('FUCK OFF') == 100
    assert value('fuck off') == 100
    assert value('wongabunga') == 100

if __name__ == "__main__":
    main()