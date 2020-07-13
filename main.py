'''n2w: convert numbers in text into words.
Usage:
    n2w [--text <text>] [--filepath <filename>]

Examples:
    $ n2w -f 'test/test_input.txt'
    eleven
    twenty-one
    $ n2w -t 'a 1 b 23'
    one
    twenty-three
'''

import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(description='converting numbers in your text')
    parser.add_argument('-f', '--filepath', help='file name as absolute path', default=None, required=False)
    parser.add_argument('-t', '--text', help='text blocks to convert', default=None, required=False)
    args = vars(parser.parse_args())
    if args['filepath'] or args['text']:
        if args['filepath'] and args['text']:
            sys.stdout.write('filepath and text cannot coexist in command line, please specify only one.')
            sys.exit(1)
        text = ''
        if args['filepath']:
            from n2w.reader import read_from_file
            try:
                text = read_from_file(args['filepath'])
            except Exception as e:
                sys.stdout.write('unable to read data from file.')
                sys.exit(1)
        elif args['text']:
            text = args['text']
        try:
            from n2w.n2w_en import Num2WordEN
            words = Num2WordEN(text).result()
            sys.stdout.write(words + os.linesep)
            sys.exit(0)
        except Exception as err:
            sys.stderr.write(str(args))
            sys.stderr.write(str(err) + os.linesep)
            sys.stderr.write(__doc__)
            sys.exit(1)


if __name__ == '__main__':
    main()
