from src import *

def test_roman_1():
    assert romanNumeral(1) == "I"

def test_roman_2():
    assert romanNumeral(2) == "II"

def test_roman_0():
    assert romanNumeral(0) == "Chiffre invalide !"

def test_roman_999999():
    assert romanNumeral(999999) == "Chiffre invalide !"

def test_roman_125():
    assert romanNumeral(125) == "CXXV"

def test_roman_1225():
    assert romanNumeral(1225) == "MCCXXV"

def test_roman_99999():
    assert romanNumeral(99999) == "X̅CI̅X̅CMXCIX"

def test_roman_958():
    assert romanNumeral(958) == "CMLVIII"

def test_roman_2002():
    assert romanNumeral(2002) == "MMII"