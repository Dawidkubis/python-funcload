#!/usr/bin/python
'''
function loading to current session
'''

import sys

def load(name, args=(), script=sys.argv[0]):
    '''
    Loads all variables from a function to current session
    name - name of function
    args - arguments of function as tuple, None by default
    script - file name of current session, sys.argv[0] by default
    '''
    import os
    import re

    ## basic asserts

    assert isinstance(args, tuple), 'args is meant to be tuple'
    assert os.path.exists(script), 'invalid path'

    def get_lines(file):

        with open(file, 'r') as f:
            return f.readlines()

    def set_lines(file, lines):

        with open(file, 'w') as f:
            f.writelines(lines)

    def get_random_file_name():

        import random
        from string import ascii_lowercase
        from functools import reduce

        def roll_name():
            return reduce((lambda a, b: a + b), [random.choice(ascii_lowercase) for i in  range(random.randint(10, 20))])

        while True:
            x = roll_name()
            if x not in os.listdir():
                return x

    def get_intend(string):

        intend = ''
        for i in string:
            if i not in (' ', '\t'):
                break
            intend += i
        return intend

    def parse_args(func_head):

        func_head = re.search(r'\(.+\)', func_head)

        if not func_head:
            return tuple()

        func_head = func_head.group()[1:-1]
        func_head = func_head.replace(',', '').split(' ')
        func_head = [i.strip() for i in func_head]

        return func_head

    def subs_args(lines, zip_args):

        from copy import deepcopy
        lines = deepcopy(lines)

        for line in lines:
		
            status = None
            i = 0
            while i < len(line):
				
                if line[i] == "'":
                    status = None if status == "'" else "'"
                elif line[i] == '"':
                    status = None if status == '"' else '"'

                if status == None:

                    for x in [i[0] in zip_args]:

                        if x[0] == line[i] and len(line) < i + len(x):
                            if i == 0 or line[i-1] in ' ', '\t':
                                pass


                i += 1

    ## open file and read lines

    lines = get_lines(script)

    ## find line with function definition

    for index, value in enumerate(lines):
        func_head = re.search(rf'def\s{name}.*', value)
        if func_head:
            lines = lines[index:]
            break
    #print(lines)

    ## check if func_head is not None, therefore function exists in script
    ## return None if function not found

    assert func_head != None, 'function not found'

    ## save intendation on func_head

    func_head = lines[0]
    lines = lines[1:]
    intend = get_intend(func_head)
    #print(intend + func_head)

    ## find end line of function

    for index, value in enumerate(lines):
        if get_intend(value) == intend:
            lines = lines[:index + 1]
            break
    #print(lines)
    #print(get_random_file_name())

    ## get function arguments

    func_args = parse_args(func_head)

    ## check if len of func_args matcher len of args

    assert len(func_args) == len(args), 'invalid number of function arguments'

    ## make a zip from function arguments and args variable

    args = list(zip(func_args, args))
    #print(args)
    print(lines)

    ## replace arg names with values

assert __name__ != '__main__', 'This module is meant to be imported!'
