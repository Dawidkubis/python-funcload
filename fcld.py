#!/usr/bin/python

import sys

def load(name, args=None, SCRIPT = sys.argv[0]):
    '''
    Loads all variables from a function to current session
    name - name of function
    args - arguments of function as tuple, None by default
    SCRIPT - file name of current session, sys.argv[0] by default
    '''

    def get_lines(file):

        with open(file, 'r') as file:
            return file.readlines()

    def set_lines(file, lines):
        
        with open(file, 'w') as file:
            file.writelines(lines)

    def get_random_file_name():
        pass

    def get_intend(string):

        intend = ''
        for i in string:
            if i not in (' ', '\t'):
                break
            intend += i
        return intend

    import re

    # open file and read lines

    lines = get_lines(SCRIPT)

    # find line with function definition

    start_line = None
    for index, value in enumerate(lines):
        func_head = re.search(rf'def\s{name}.*', value)
        if func_head:
            lines = lines[index:]
            break
    #print(lines)

    # check if func_head is not None, therefore function exists in SCRIPT
    # return None if function not found

    if not func_head:
        print('func not found')
        return

    # save intendation on func_head
    
    func_head = lines[0] 
    intend = get_intend(func_head)
    #print(intend + func_head)

    # find end line of function

    for index, value in enumerate(lines[1:]):
        if get_intend(value) == intend:
            lines = lines[:index + 1]
            break

assert __name__ != '__main__', 'This module is meant to be imported!'
