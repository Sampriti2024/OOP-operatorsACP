class RomanNumeralConverter:


    def __init__(self, number):
        self.number = number

    def convert(self):

        roman_numerals = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        roman_numeral = ""
        for value, symbol in roman_numerals.items():
            while self.number >= value:
                roman_numeral += symbol
                self.number -= value

        return roman_numeral

if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    converter = RomanNumeralConverter(number)
    roman_numeral = converter.convert()
    print(f"The Roman numeral for {number} is {roman_numeral}")