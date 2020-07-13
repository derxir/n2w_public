import re
from abc import ABC, abstractmethod
from typing import List

# this arrangement is easier for code review and modification later on
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


class AbstractConverter(ABC):
    """
    Base Converter that extracts, converts delegately, and formats output. It can be extended by language specific converters
    which only implement method to conver a single number to word
    """

    def __init__(self, text):
        self.text = text
        self.nums = self.extract(text)
        self.words = self.convert(self.nums)
        self.erro = 'number invalid'

    def extract(self, text) -> List[str]:
        """
        extract all valid numbers in given text
        :param text
        :return valid numbers in text
        """
        if not text:
            return []
        words = re.split(r'[A-Za-z][ ]+|[ ]+[A-Za-z]|[ ]{2}[ ]*', text)
        return [w.strip() for w in words if self._is_num(w)]

    def convert(self, nums: List[str]) -> List[str]:
        """
        convert all valid numbers to words.
        :param nums: list of extracted numbers from the text
        :return numbers in words
        """
        return [self.convert_single_number(num) for num in nums]

    def result(self) -> str:
        """
        return the converted numbers in words. If multiple numbers are converted, words are concatenated with '\n' chars
        """
        if not self.words or not all(self.words):
            return self.erro
        if len(self.words) == 1:
            return self.words[0]
        s = ''
        for w in self.words:
            s = s + w + '\n'
        return s

    @abstractmethod
    def convert_single_number(self, num: str) -> str:
        raise NotImplementedError

    def _is_num(self, text: str) -> bool:
        # defensive
        if text is None or text == '':
            return False
        # check against selected char set
        text = text.strip()
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
            tokens = text.split(',')[::-1]
            for token in tokens[:-1]:
                if len(token) != 3:
                    return False
        return True

    def _split(self, num: str) -> List[str]:
        """
        split given integer into group of digits with length ranged from 1 to 3
        :param num as string
        :return the list of digit groups in reverse order
        """
        # remove minus sign when split
        if num.startswith('-'):
            num = num[1:]
        if ',' in num:
            return num.split(',')
        num = num[::-1]
        groups = [num[i:i + 3][::-1] for i in range(0, len(num), 3)][::-1]
        return groups

    def __str__(self):
        return self.result()
