#write code here
def roman_numeral(num : int):
    result = ""
    num_str = str(num)

    if num > 99999 or num < 1:
        return "Chiffre invalide !"
    if num > 9999:
        dml = dizaines_milliers()
        result += dml[num_str[:1]]
        num_str = num_str[1:]
    if num > 999:
        mil = milliers()
        result += mil[num_str[:1]]
        num_str = num_str[1:]
    if num > 99:
        cen = centaines()
        result += cen[num_str[:1]]
        num_str = num_str[1:]
    if num > 9:
        diz = dizaines()
        result += diz[num_str[:1]]
        num_str = num_str[1:]


    uni = unit()
    result += uni[num_str]

    return result

def arabicNumeral(num: str):
    digits = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8,
              "IX": 9,
              "X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70,
              "LXXX": 80, "XC": 90,
              "C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700,
              "DCCC": 800, "CM": 900,
              "M": 1000, "MM": 2000, "MMM": 3000, "4": "I̅V̅", "5": "V̅", "6": "V̅I̅",
              "7": "V̅I̅I̅", "8": "V̅I̅I̅I̅", "9": "I̅X̅",
              "1": "X̅", "2": "X̅X̅", "3": "X̅X̅X̅", "4": "X̅L̅",
              "5": "L̅", "6": "L̅X̅", "7": "L̅X̅X̅", "8": "L̅X̅X̅X̅", "9": "X̅C"}
    result = 0
    base = num
    tmp = ""

    while base != "":
        tmp = base[:1]
        while tmp in

    return result

def dizaines_milliers():
    return {"0": "", "1": "X̅", "2": "X̅X̅", "3": "X̅X̅X̅", "4": "X̅L̅", "5": "L̅", "6": "L̅X̅", "7": "L̅X̅X̅",
            "8": "L̅X̅X̅X̅", "9": "X̅C"}


def milliers():
    return {"0": "", "1": "M", "2": "MM", "3": "MMM", "4": "I̅V̅", "5": "V̅", "6": "V̅I̅", "7": "V̅I̅I̅", "8":
        "V̅I̅I̅I̅", "9": "I̅X̅"}


def centaines():
    return {"0": "", "1": "C", "2": "CC", "3": "CCC", "4": "CD", "5": "D", "6": "DC", "7": "DCC", "8": "DCCC",
            "9": "CM"}


def dizaines():
    return {"0": "", "1": "X", "2": "XX", "3": "XXX", "4": "XL", "5": "L", "6": "LX", "7": "LXX", "8": "LXXX",
            "9": "XC"}


def unit():
    return {
        "0": "",
        "1": "I",
        "2": "II",
        "3": "III",
        "4": "IV",
        "5": "V",
        "6": "VI",
        "7": "VII",
        "8": "VIII",
        "9": "IX"
    }