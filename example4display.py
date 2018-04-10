#!/usr/bin/env python3

import os


def get_path(fname):
    """Return file's path or empty string if no path."""
    import pdb; pdb.set_trace()
    head, tail = os.path.split(fname)
    for char in tail:
        pass  # Check filename char
    return head


filename = __file__
filename_path = get_path(filename)
print(f'path = {filename_path}')

'''
-> head, tail = os.path.split(fname)
(Pdb) ll
  6  	def get_path(fname):
  7  	    """Return file's path or empty string if no path."""
  8  	    import pdb; pdb.set_trace()
  9  ->	    head, tail = os.path.split(fname)
 10  	    for char in tail:
 11  	        pass  # Check filename char
 12  	    return head
(Pdb) b 11
Breakpoint 1 at /Users/mahendra/projects/pdb_tutorial/example4display.py:11
(Pdb) c
> /Users/mahendra/projects/pdb_tutorial/example4display.py(11)get_path()
-> pass  # Check filename char
(Pdb) display char
display char: 'e'
(Pdb) c
> /Users/mahendra/projects/pdb_tutorial/example4display.py(11)get_path()
-> pass  # Check filename char
display char: 'x'  [old: 'e']
(Pdb)
> /Users/mahendra/projects/pdb_tutorial/example4display.py(11)get_path()
-> pass  # Check filename char
display char: 'a'  [old: 'x']
(Pdb)
> /Users/mahendra/projects/pdb_tutorial/example4display.py(11)get_path()
-> pass  # Check filename char
display char: 'm'  [old: 'a']

--

(Pdb) ll
  6  	def get_path(fname):
  7  	    """Return file's path or empty string if no path."""
  8  	    import pdb; pdb.set_trace()
  9  ->	    head, tail = os.path.split(fname)
 10  	    for char in tail:
 11  	        pass  # Check filename char
 12  	    return head
(Pdb) b 11
Breakpoint 1 at /Users/mahendra/projects/pdb_tutorial/example4display.py:11
(Pdb) c
> /Users/mahendra/projects/pdb_tutorial/example4display.py(11)get_path()
-> pass  # Check filename char
(Pdb) display char
display char: 'e'
(Pdb) display fname
display fname: './example4display.py'
(Pdb) display head
display head: '.'
(Pdb) display tail
display tail: 'example4display.py'
(Pdb) c
> /Users/mahendra/projects/pdb_tutorial/example4display.py(11)get_path()
-> pass  # Check filename char
display char: 'x'  [old: 'e']
(Pdb) display
Currently displaying:
char: 'x'
fname: './example4display.py'
head: '.'
tail: 'example4display.py'
'''
