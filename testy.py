#!/usr/bin/python -i

def hey(arg, arg2):
    a = 2
    b = 4
    skk = '42'
    if skk == '42':
        print('gah')
    print('IT WORKED', arg)
    print('ok')

from fcld import load
cache = load('hey', ('lll', 'zzz'))
