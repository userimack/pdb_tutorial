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
"""
(Pdb) ll
  6  	def get_path(fname):
  7  	    """Return file's path or empty string if no path."""
  8  	    import pdb; pdb.set_trace()
  9  ->	    head, tail = os.path.split(fname)
 10  	    for char in tail:
 11  	        pass  # Check filename char
 12  	    return head
(Pdb) unt
> /Users/mahendra/projects/pdb_tutorial/example4unt.py(10)get_path()
-> for char in tail:
(Pdb)
> /Users/mahendra/projects/pdb_tutorial/example4unt.py(11)get_path()
-> pass  # Check filename char
(Pdb)
> /Users/mahendra/projects/pdb_tutorial/example4unt.py(12)get_path()
-> return head
(Pdb) p char, tail
('y', 'example4unt.py')

"""
