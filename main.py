import os

parent_dir = input('Parent directory: ')
name = input('Name of the project: ')
author = input('Author: ')

path = os.path.join(parent_dir, name)
os.mkdir(path)
