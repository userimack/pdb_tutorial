#!/usr/bin/env python3

import util

filename = __file__
import pdb; pdb.set_trace()
filename_path = util.get_path(filename)
print(f'path = {filename_path}')

"""
-> filename_path = util.get_path(filename)
(Pdb) b util:5
Breakpoint 1 at /Users/mahendra/projects/pdb_tutorial/util.py:5
(Pdb) c
> /Users/mahendra/projects/pdb_tutorial/util.py(5)get_path()
-> return head
(Pdb) p filename, head, tail
('example4.py', '', 'example4.py')

----

(Pdb) b util.get_path
Breakpoint 1 at /Users/mahendra/projects/pdb_tutorial/util.py:1
(Pdb) c
> /Users/mahendra/projects/pdb_tutorial/util.py(3)get_path()
-> import os
(Pdb) p filename
'example4.py'
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at /Users/mahendra/projects/pdb_tutorial/util.py:1
	breakpoint already hit 1 time
(Pdb) disable 1
Disabled breakpoint 1 at /Users/mahendra/projects/pdb_tutorial/util.py:1
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep no    at /Users/mahendra/projects/pdb_tutorial/util.py:1
	breakpoint already hit 1 time
(Pdb) enable 1
Enabled breakpoint 1 at /Users/mahendra/projects/pdb_tutorial/util.py:1
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at /Users/mahendra/projects/pdb_tutorial/util.py:1
	breakpoint already hit 1 time
(Pdb) cl
Clear all breaks? y
Deleted breakpoint 1 at /Users/mahendra/projects/pdb_tutorial/util.py:1
----

(Pdb) b util:5, not head.startswith("/")
Breakpoint 1 at /Users/mahendra/projects/pdb_tutorial/util.py:5
(Pdb) c
> /Users/mahendra/projects/pdb_tutorial/util.py(5)get_path()
-> return head
(Pdb) p head
'.'
(Pdb) a
filename = './example4.py'

"""
