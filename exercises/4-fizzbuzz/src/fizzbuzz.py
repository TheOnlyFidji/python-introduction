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

def fizzbuzz_from_range(lower, upper):
    result = ""
    i = lower
    while i <= upper:
        result += fizzbuzz(i)+", "
        i += 1
    result = result[:-2]
    return result

