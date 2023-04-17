from numb3rs import validate
import sys

def test_positive():
    assert validate("127.0.0.255") == True
    assert validate("255.255.255.255") == True



def test_negative():
    assert validate("cat") == False
    assert validate("259.259.259.259") == False
    assert validate("10.20.30.1000") == False
    assert validate("10.300.20.20") == False
