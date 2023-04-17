from plates import is_valid

def main ():
    test_1()
    test_2()
    test_3()
    test_4()

def test_1():
    assert is_valid('CS50') == True
    assert is_valid('ABCD') == True

def test_2():
    assert is_valid('K') == False
    assert is_valid('K250') == False


def test_3():
    assert is_valid('2CSO') == False
    assert is_valid('KT05YT') == False
    assert is_valid('KT51OO') == False

def test_4():
    assert is_valid('KT05') == False
    assert is_valid('NARNIA234') == False
    assert is_valid('KTA 50') == False


if __name__ == "__main__":
    main()