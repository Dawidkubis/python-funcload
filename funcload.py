#!/usr/bin/python

import re
import random
import sys
import os

def load(name, args=None):
    # get name of file

    SCRIPT = sys.argv[0]

    # open file and read lines

    with open(SCRIPT, 'r') as self:
        lines = self.readlines()
    
    # find line with function definition
    
    start_line = None
    for index, value in enumerate(lines):
        func_head = re.search(f'def\s{name}.*', value)
        if func_head:
            start_line = index
            break

    # check if func_head is not None, therefore function exists in SCRIPT
    # return None if function not found

    if not func_head:
        return

if __name__ == '__main__':
    pass
