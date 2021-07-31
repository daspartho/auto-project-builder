import os

def ask_input():
    parent_dir = input('Parent directory: ')
    name = input('Name of the project: ')
    author = input('Author: ')
    return parent_dir, name, author

def make_dir(parent_dir, name):
    path = os.path.join(parent_dir, name)
    os.mkdir(path)
    print(f'Created directory {path}')
    return path

def createREADME(parent_dir, name, author):
    path = parent_dir+'\README.md'
    README = open(path , 'w')
    
    content = f"""Welcome to {name}
Created by {author}"""
    
    README.write(content)
    README.close()
    print(f'Created file {path}')

def createMain(parent_dir, name):
    path = parent_dir+'\main.py'
    main_file = open(path, 'w')
    
    boilerplate=f"""if __name__ == '__main__':
    print('Welcome to {name}')"""
                
    main_file.write(boilerplate)
    main_file.close()
    print(f'Created file {path}')

def createTODO(parent_dir, name):
    path = parent_dir+'\TODO.md'
    TODO = open(path, 'w')
    
    content = f'TODO for {name}'
    
    TODO.write(content)
    TODO.close()
    print(f'Created file {path}')
    
def main():
    parent_dir, name, author = ask_input()
    path = make_dir(parent_dir, name)
    createREADME(path, name, author)
    createMain(path, name)
    createTODO(path, name)
    print('Done!')

if __name__ == '__main__':
    main()
