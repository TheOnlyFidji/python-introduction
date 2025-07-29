from src import *

def test_roman_1():
    assert roman_numeral(1) == "I"

def test_roman_2():
    assert roman_numeral(2) == "II"

def test_roman_0():
    assert roman_numeral(0) == "Chiffre invalide !"

def test_roman_999999():
    assert roman_numeral(999999) == "Chiffre invalide !"

def test_roman_125():
    assert roman_numeral(125) == "CXXV"

def test_roman_1225():
    assert roman_numeral(1225) == "MCCXXV"

def test_roman_99999():
    assert roman_numeral(99999) == "X̅CI̅X̅CMXCIX"

def test_roman_958():
    assert roman_numeral(958) == "CMLVIII"

def test_roman_2002():
    assert roman_numeral(2002) == "MMII"

def test_arabic_1():
    assert arabic_numeral("I") == 1

def test_arabic_2():
    assert arabic_numeral("II") == 2

def test_arabic_2002():
    assert arabic_numeral("MMII") == 2002

def test_arabic_678():
    assert arabic_numeral("DCLXXVIII") == 678

def test_arabic_3888():
    assert arabic_numeral("MMMDCCCLXXXVIII") == 3888