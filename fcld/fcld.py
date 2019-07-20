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

    assert type(args) in (dict, tuple), 'args is meant to be tuple'
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
                return x+'.py'

    def get_indent(string):

        indent = ''
        for i in string:
            if i not in (' ', '\t'):
                break
            indent += i
        return indent

    def parse_args(func_head):

        func_head = re.search(r'\(.+\)', func_head)

        if not func_head:
            return tuple()

        func_head = func_head.group()[1:-1]
        func_head = func_head.replace(',', '').split(' ')
        func_head = [i.strip() for i in func_head]

        return func_head

    def add_values(lines, zip_args):

        from copy import deepcopy

        lines = deepcopy(lines)
        values = []

        for i in zip_args:
            if isinstance(zip_args[i], str):
                values.append(f"{i} = '{zip_args[i]}'\n")
            else:
                values.append(f'{i} = {zip_args[i]}\n')

        return values + lines

    def untab(lines, indent):

        return [i.replace(indent, '', 1) for i in lines]

    ## open file and read lines

    lines = get_lines(script)

    ## find line with function definition

    for index, value in enumerate(lines):
        func_head = re.search(rf'def\s{name}.*', value)
        if func_head:
            lines = lines[index:]
            break

    ## check if func_head is not None, therefore function exists in script
    ## return None if function not found

    assert func_head is not None, 'function not found'

    ## save indentation on func_head and first line of code

    func_head = lines[0]
    lines = lines[1:]
    indent = get_indent(func_head)
    indent_code = get_indent(lines[0])

    ## find end line of function

    for index, value in enumerate(lines):
        if get_indent(value) == indent:
            lines = lines[:index + 1]
            break

    ## get function arguments

    func_args = parse_args(func_head)

    ## check if len of func_args matcher len of args

    assert len(func_args) == len(args), 'invalid number of function arguments'
    if isinstance(args, dict):
        for i in args:
            assert i in func_args, f'invalid argument name: {i}, arguments are {func_args}'
    ## make a dict from zip from function arguments and args variable if not dict

    args = dict(zip(func_args, args)) if isinstance(args, tuple) else args

    ## untab lines

    lines = untab(lines, indent_code)

    ## add variable values

    lines = add_values(lines, args)

    ## write lines to random file

    name = get_random_file_name()
    set_lines(name, lines)

    ## import file

    from importlib import import_module
    print('-'*10, 'loading module')
    cache = import_module(name[:-3])
    print('-'*10)

    ## delete file

    os.remove(name)

    ## return cache

    return cache

assert __name__ != '__main__', 'This module is meant to be imported!'
