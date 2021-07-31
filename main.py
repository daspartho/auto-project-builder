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

def createREADME(parent_dir, name, author):
    README = open(parent_dir+'\README.md', 'w')
    
    content = f"""Welcome to {name}
Created by {author}"""
    
    README.write(content)
    README.close()

def createMain(parent_dir, name):
    main_file = open(parent_dir+'\main.py', 'w')
    
    boilerplate=f"""if __name__ == '__main__':
    print('Welcome to {name}')"""
                
    main_file.write(boilerplate)
    main_file.close()

def createTODO(parent_dir, name):
    TODO = open(parent_dir+'\TODO.md', 'w')
    
    content = f'TODO for {name}'
    
    TODO.write(content)
    TODO.close()
    
def main():
    parent_dir, name, author = ask_input()
    path = make_dir(parent_dir, name)
    createREADME(path, name, author)
    createMain(path, name)
    createTODO(path, name)

if __name__ == '__main__':
    main()
