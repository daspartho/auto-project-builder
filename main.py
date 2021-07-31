import string
import os

def is_valid_project_name(project_name):

    LEGAL_PROJECT_NAME_CHARS = (
    list(string.ascii_lowercase) +
    list(string.ascii_uppercase) +
    [str(x) for x in range(0, 10)] +
    ['-', '_'])

    for ch in project_name:
        if ch not in LEGAL_PROJECT_NAME_CHARS:
            return False

    if len(project_name)<2 or len(project_name)>20:
        return False

    return True

def is_valid_author_name(author_name):
    return len(author_name) > 0

def ask_input():
    parent_dir = input('Parent directory: ')

    while True:
        name = input('Name of the project: ')
        if is_valid_project_name(name):
            break
        print('Invalid Project Name! Try Again!')

    while True:
        author = input('Author: ')
        if is_valid_author_name(author):
            break
        print('Invalid Author Name! Try Again!')
        
    return parent_dir, name, author

def make_dir(parent_dir, name):
    path = os.path.join(parent_dir, name)
    os.mkdir(path)
    print(f'Created directory {path}')
    return path

def createREADME(parent_dir, name, author):
    path = parent_dir+'\README.md'
    README = open(path , 'w')
    
    content = f"Welcome to {name}\nCreated by {author}"
    
    README.write(content)
    README.close()
    print(f'Created file {path}')

def createMain(parent_dir, name):
    path = parent_dir+'\main.py'
    main_file = open(path, 'w')
    
    content = f"if __name__ == '__main__':\n\tprint('Welcome to {name}')"
                
    main_file.write(content)
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
