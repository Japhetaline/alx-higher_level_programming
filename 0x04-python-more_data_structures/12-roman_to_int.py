#!/usr/bin/python3

def romian_to_int(roman_string):
    """
    Converts roman numeral character into integer
    """

    if roman_string is None or type(roman_string) is not str:
        return (0)
    roman_book = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }
    roman_file = list(roman_string.upper())
    outcome = 0
    prev = 0
    for note in roman_file:
        if note in roman_book:
            outcome += roman_book[note]
            if roman_book[note] > prev:
                outcome -= prev * 2
                prev = roman_book[note]
            else:
                return (0)
            return (outcome)
