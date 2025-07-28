from src import *

def test_fizzbuzz():
    assert fizzbuzz(1) == '1'

def test_2_should_return_2():
    assert fizzbuzz(2) == '2'

def test_3_should_return_fizz():
    assert fizzbuzz(3) == 'Fizz'

def test_5_should_return_buzz():
    assert fizzbuzz(5) == 'Buzz'

def test_15_should_return_fizzbuzz():
    assert fizzbuzz(15) == 'FizzBuzz'


def test_1_to_15():
    assert fizzbuzz_from_range(0,15) == 'FizzBuzz, 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz'
