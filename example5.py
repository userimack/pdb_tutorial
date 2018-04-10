#!/usr/bin/env python3

import fileutil


def get_file_info(full_fname):
    file_path = fileutil.get_path(full_fname)
    return file_path


filename = __file__
filename_path = get_file_info(filename)
print(f'path = {filename_path}')

'''
(Pdb) w
  /Users/mahendra/projects/pdb_tutorial/example5.py(12)<module>()
-> filename_path = get_file_info(filename)
  /Users/mahendra/projects/pdb_tutorial/example5.py(7)get_file_info()
-> file_path = fileutil.get_path(full_fname)
> /Users/mahendra/projects/pdb_tutorial/fileutil.py(5)get_path()
-> head, tail = os.path.split(fname)
(Pdb) u
> /Users/mahendra/projects/pdb_tutorial/example5.py(7)get_file_info()
-> file_path = fileutil.get_path(full_fname)
(Pdb) p full_fname
'./example5.py'
(Pdb) d
> /Users/mahendra/projects/pdb_tutorial/fileutil.py(5)get_path()
-> head, tail = os.path.split(fname)
(Pdb) p fname
'./example5.py'

'''
