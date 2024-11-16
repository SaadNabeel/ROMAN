class IntegerToRoman:
    def __init__(self):
       
        self.value_map = [
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def convert(self, num):
        
        roman_numeral = ''
        for value, numeral in self.value_map:
            while num >= value:
                roman_numeral += numeral
                num -= value
        return roman_numeral



if __name__ == "__main__":
    converter = IntegerToRoman()
    number = int(input("Enter an integer: "))
    print("The Roman numeral for ",number,"is",converter.convert(number))
