from enum import Enum
from typing import List

"""
  private static String convertLessThanOneThousand(int number) {
    String soFar;

    if (number % 100 < 20){
      soFar = numNames[number % 100];
      number /= 100;
    }
    else {
      soFar = numNames[number % 10];
      number /= 10;

      soFar = tensNames[number % 10] + soFar;
      number /= 10;
    }
    if (number == 0) return soFar;
    return numNames[number] + " hundred" + soFar;
  }
"""
VALID_CHARSET = {'0',
                 '1',
                 '2',
                 '3',
                 '4',
                 '5',
                 '6',
                 '7',
                 '8',
                 '9',
                 ',',
                 '-'}

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


class CONCAT(Enum):
    COMMA = ',',
    SPACE = ' ',
    DASH = '-'


class Num2Word:

    def __init__(self, text):
        self.text = text
        self.nums = self.extract(text)
        self.words = self.convert(self.nums)
        self.erro = 'number invalid'

    def extract(self, text) -> List[str]:
        """
        extract all valid numbers in text
        :param text
        :return valid numbers in text
        """
        if not text:
            return []
        words = text.split()
        return [w for w in words if self.is_num(w)]

    def result(self) -> str:
        if not self.words:
            return self.erro
        if len(self.words) == 1:
            return self.words[0]
        s = ''
        for w in self.words:
            s = s + w + '\n'
        return s

    def is_num(self, text: str) -> bool:
        """
        Rules:
        1. number cam only start with any digit in 1-9 or '-' sign.
        2. number can only have characters in set {',','.'} otherthan digits.
        3. character ',' can only exist on position of index of n/3 given the number is read as string revertly.
        """
        if text == None or text == '':
            return False
        # check against selected char set
        for c in text:
            if c not in VALID_CHARSET:
                return False
        if '-' in text and text.index('-') != 0:
            return False
        # check for invalid leading chars
        if len(text) > 1 and text[0] in {'0', ','}:
            return False
        # check for invalid , positions
        if ',' in text:
            if len(text) < 4:
                return False
            if len(text) >= 4:
                return True  # TODO
        return True

    def convert(self, nums: List[str]) -> List[str]:
        """
        convert all valid numbers to words.
        :param nums: list of extracted numbers from the text
        :return numbers in words
        """
        return [self.convert_to_word(num) for num in nums]

    def _split(self, num: str) -> List[str]:
        """
        split given integer into group of digits with length ranged from 1 to 3
        :param integer
        :return the list of digit groups in reverse order
        """
        if ',' in num:
            return num.split(',')
        num = num[::-1]
        groups = [num[i:i + 3][::-1] for i in range(0, len(num), 3)][::-1]
        return groups

    def convert_to_word(self, num: str) -> List[str]:
        digit_group = self._split(num)
        output = ''
        count_groups = 0
        digit_words = []
        for digits in digit_group:
            digit_words.append(self.convert_below_thousand(digits))
        sufx = SUFFIXES[:len(digit_words)][::-1]
        while digit_words:
            w = digit_words.pop(0)
            s = sufx.pop(0)
            ws =  w + s
            if output:
                if w == ZERO:
                    continue
                if not digit_words: # last group
                    output = output + (' and ' if 'and' not in w else ', ')
                else:
                    output = output + ', '
            output = output + ws
        return output

    def convert_below_thousand(self, num: str):
        n = int(num)
        if n == 0:
            return ZERO
        i, r = divmod(n, 100)
        if r < 20:
            word = BELOW_20[r]
            n = i
        else:
            word = BELOW_20[n % 10]
            n = n // 10

            word = TENS[n % 10] + ('-' if word else '') + word
            n = n // 10
        if n != 0:
            word = BELOW_20[n] + ' hundred' +  (' and ' if word else '') + word
        return word

    def __len__(self):
        """return the number of converted numbers"""
        return len(self.words)
