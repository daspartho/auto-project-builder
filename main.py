import os

def ask_input():
    parent_dir = input('Parent directory: ')
    name = input('Name of the project: ')
    author = input('Author: ')
    return parent_dir, name, author

def make_dir(parent_dir, name):
    path = os.path.join(parent_dir, name)
    os.mkdir(path)
    return path

def CreateREADME(parent_dir, name, author):
    README = open(parent_dir+'\README.md', 'w')
    README.write(f'Name: {name}\nAuthor: {author}')
    README.close()

def main():
    parent_dir, name, author = ask_input()
    path = make_dir(parent_dir, name)
    CreateREADME(path, name, author)

if __name__ == '__main__':
    main()
