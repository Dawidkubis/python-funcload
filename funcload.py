#!/usr/bin/python

def get_intend(string):

    intend = ''
    for i in string:
        if i not in (' ', '\t'):
            break
        intend += i
    return intend

def load(name, args=None):

    import re

    def get_lines(file):

        with open(file, 'r') as file:
            return file.readlines()

    def set_lines(file):

        import random


    # get name of file

    SCRIPT = sys.argv[0]

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

    #print(lines)

    # 
    
if __name__ == '__main__':
    pass
