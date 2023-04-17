from  um import count

def test_r():

    assert count("um") == 1
    assert count("um um") == 2
    assert count("Um") == 1

def test_w():
    assert count("Hi what up") == 0
    assert count("album") == 0


