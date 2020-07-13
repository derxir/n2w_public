from n2w.n2w_en import *


def test_given_testcases():
    assert Num2WordEN('The pump is 536 deep underground.').result() == 'five hundred and thirty-six'
    assert Num2WordEN('We processed 9121 records.').result() == 'nine thousand, one hundred and twenty-one'
    assert Num2WordEN('Variables reported as having a missing type #65678.').result() == 'number invalid'
    assert Num2WordEN('Interactive and printable 10022 ZIP code.').result() == 'ten thousand and twenty-two'
    assert Num2WordEN(
        'The database has 66723107008 records.').result() == 'sixty-six billion, seven hundred and twenty-three million, one hundred and seven thousand and eight'
    assert Num2WordEN('I received 23 456,9 KGs.').result() == 'number invalid'


def test_invalid_input():
    assert Num2WordEN(None).result() == 'number invalid'
    assert Num2WordEN('None').result() == 'number invalid'
    assert Num2WordEN('').result() == 'number invalid'
    assert Num2WordEN('01').result() == 'number invalid'
    assert Num2WordEN('+1').result() == 'number invalid'
    assert Num2WordEN('&1').result() == 'number invalid'
    assert Num2WordEN('#1').result() == 'number invalid'
    assert Num2WordEN('1-').result() == 'number invalid'
    assert Num2WordEN('1,').result() == 'number invalid'
    assert Num2WordEN('1,00').result() == 'number invalid'
    assert Num2WordEN(',1,00').result() == 'number invalid'
    assert Num2WordEN('1 1').result() == 'number invalid'


def test_should_match_double_single_numbers():
    assert Num2WordEN('0').result() == 'zero'
    assert Num2WordEN('1').result() == 'one'
    assert Num2WordEN('2').result() == 'two'
    assert Num2WordEN('3').result() == 'three'
    assert Num2WordEN('4').result() == 'four'
    assert Num2WordEN('5').result() == 'five'
    assert Num2WordEN('6').result() == 'six'
    assert Num2WordEN('7').result() == 'seven'
    assert Num2WordEN('8').result() == 'eight'
    assert Num2WordEN('9').result() == 'nine'


def test_should_match_double_digit_numbers():
    assert Num2WordEN('10').result() == 'ten'
    assert Num2WordEN('11').result() == 'eleven'
    assert Num2WordEN('12').result() == 'twelve'
    assert Num2WordEN('13').result() == 'thirteen'
    assert Num2WordEN('14').result() == 'forteen'
    assert Num2WordEN('15').result() == 'fifteen'
    assert Num2WordEN('16').result() == 'sixteen'
    assert Num2WordEN('17').result() == 'seventeen'
    assert Num2WordEN('18').result() == 'eighteen'
    assert Num2WordEN('19').result() == 'nineteen'
    assert Num2WordEN('20').result() == 'twenty'
    assert Num2WordEN('21').result() == 'twenty-one'
    assert Num2WordEN('31').result() == 'thirty-one'
    assert Num2WordEN('41').result() == 'forty-one'
    assert Num2WordEN('51').result() == 'fifty-one'
    assert Num2WordEN('61').result() == 'sixty-one'
    assert Num2WordEN('71').result() == 'seventy-one'
    assert Num2WordEN('81').result() == 'eighty-one'
    assert Num2WordEN('91').result() == 'ninety-one'
    assert Num2WordEN('99').result() == 'ninety-nine'


def test_should_deal_with_zeros_inside():
    assert Num2WordEN('100').result() == 'one hundred'
    assert Num2WordEN('101').result() == 'one hundred and one'
    assert Num2WordEN('1000').result() == 'one thousand'
    assert Num2WordEN('1101').result() == 'one thousand, one hundred and one'
    assert Num2WordEN('10000').result() == 'ten thousand'
    assert Num2WordEN('10000000').result() == 'ten million'
    assert Num2WordEN('10000000000').result() == 'ten billion'
    assert Num2WordEN('10000000000000').result() == 'ten trillion'
    assert Num2WordEN('10000000000001').result() == 'ten trillion and one'
    assert Num2WordEN('10000000000100').result() == 'ten trillion and one hundred'


def test_should_handle_arbitrary_spacing():
    assert Num2WordEN('a  1   c   2  b').result() == 'one\ntwo\n'
    assert Num2WordEN('1   c   2').result() == 'one\ntwo\n'
    assert Num2WordEN('1     2').result() == 'one\ntwo\n'


def test_should_use_concatenators_properly():
    assert Num2WordEN('111').result() == 'one hundred and eleven'
    assert Num2WordEN('1111').result() == 'one thousand, one hundred and eleven'
    assert Num2WordEN('1011').result() == 'one thousand and eleven'


def test_should_match_multiple_valid_numbers():
    assert Num2WordEN('abc 123 ebd 45 efg 1000').result() == 'one hundred and twenty-three\nforty-five\none thousand\n'


def test_should_match_max_supported_number():
    assert Num2WordEN(
        '999,999,999,999,999').result() == 'nine hundred and ninety-nine trillion, nine hundred and ninety-nine billion, ' + \
           'nine hundred and ninety-nine million, nine hundred and ninety-nine thousand, ' + \
           'nine hundred and ninety-nine'
    assert Num2WordEN('1,000,000,000,000,000').result() == 'number invalid'
    assert Num2WordEN('999,999,999,999,999,999').result() == 'number invalid'


def test_should_match_negative_number():
    assert Num2WordEN('-1').result() == 'minus one'
    assert Num2WordEN('-0').result() == 'minus zero'
    assert Num2WordEN('-555').result() == 'minus five hundred and fifty-five'
    assert Num2WordEN('-5,000').result() == 'minus five thousand'
