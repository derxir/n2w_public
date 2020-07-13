"""
Utility module for IO
"""


def read_from_file(filename):
    txt = ''
    with open(filename, 'r') as f:
        for line in f:
            l = line.rstrip()
            txt = txt + ' ' + l
    return txt
