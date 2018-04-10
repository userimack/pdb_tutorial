#!/usr/bin/env python3

import os


def get_path(filename):
    """Return file's path or empty string if no path."""
    head, tail = os.path.split(filename)
    import pdb; pdb.set_trace()
    return head


filename = __file__
print(f'path = {get_path(filename)}')

"""
(Pdb) ll
  6  	def get_path(filename):
  7  	    """Return file's path or empty string if no path."""
  8  	    head, tail = os.path.split(filename)
  9  	    import pdb; pdb.set_trace()
 10  ->	    return head
(Pdb) p get_path
<function get_path at 0x1046adf28>
(Pdb) p filename
'ex2.py'
(Pdb) p head, tail
('', 'ex2.py')
(Pdb) p getattr(get_path, '__doc__'
*** SyntaxError: unexpected EOF while parsing
(Pdb) p getattr(get_path, '__doc__')
"Return file's path or empty string if no path."
(Pdb) p [os.path.split(p)[1] for p in os.path.sys.path]
['pdb_tutorial', 'python36.zip', 'python3.6', 'lib-dynload', 'site-packages', 'site-packages', 'site-packages']
(Pdb) pp [os.path.split(p)[1] for p in os.path.sys.path]
['pdb_tutorial',
 'python36.zip',
 'python3.6',
 'lib-dynload',
 'site-packages',
 'site-packages',
 'site-packages']

"""
