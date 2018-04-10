#!/usr/bin/env python3
"""
(Pdb) p filename
'ex1.py'

"""

filename = __file__
import pdb; pdb.set_trace()
print(f'path = {filename}')
