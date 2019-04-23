"""
Use this class for any tests relating to Shortcut class
"""
from shortcut import Shortcut

keys = ['ctrl', 'c']
copy = Shortcut(keys, 'Copy text')
print(copy.getHotKey())
print(copy.getKeys())
print(copy.getDescription())
