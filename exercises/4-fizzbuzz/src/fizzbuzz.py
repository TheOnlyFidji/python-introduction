def fizzbuzz(number: int) -> str:
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"

    if result != "":
        return result
    else:
        return str(number)