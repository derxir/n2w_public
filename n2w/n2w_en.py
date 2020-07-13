from n2w.base import AbstractConverter

ZERO = 'zero'

BELOW_20 = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'forteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

TENS = [
    '',
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
    'hundred',
]

SUFFIXES = [
    '', ' thousand', ' million', ' billion', ' trillion'
]


class Num2WordEN(AbstractConverter):

    def __init__(self, text):
        super().__init__(text)

    def convert_single_number(self, num: str) -> str:
        output = ''
        digit_words = []

        digit_group = self._split(num)
        # defensive programming
        if len(digit_group) > len(SUFFIXES):
            return output

        for digits in digit_group:
            digit_words.append(self._convert_natual_int_below_thousand(digits))
        sufx = SUFFIXES[:len(digit_words)][::-1]
        while digit_words:
            w = digit_words.pop(0)
            s = sufx.pop(0)
            ws = w + s
            if output:
                if w == ZERO:
                    continue
                if not digit_words:  # last group
                    output = output + (' and ' if 'and' not in w else ', ')
                else:
                    output = output + ', '
            output = output + ws
        # handling negative numbers
        if num.startswith('-'):
            output = 'minus ' + output
        return output

    def _convert_natual_int_below_thousand(self, num: str):
        n = int(num)
        if n == 0:
            return ZERO
        i, r = divmod(n, 100)
        if r < 20:
            word = BELOW_20[r]
            n = i
        else:
            n, r = divmod(n, 10)
            word = BELOW_20[r]

            n, r = divmod(n, 10)
            word = TENS[r] + ('-' if word else '') + word
        if n != 0:
            word = BELOW_20[n] + ' hundred' + (' and ' if word else '') + word
        return word
