import string
import os

def is_valid_project_name(project_name):
    '''Checks if project name is valid and return boolean value.'''

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
    '''Checks if author name is valid and returns boolean value.'''
    
    return len(author_name) > 0 and author_name.isalpha()

def ask_input():
    '''Asks user for parent directory, name of the project and author name and then returns a tuple consisting input.'''
    
    parent_dir = input('Parent directory: ')

    while True:
        name = input('Name of the project: ')
        if is_valid_project_name(name):
            break
        print('Invalid Project Name! Try Again!')
        print('Project name should contains only letters, dashes and numbers, and is between 2 and 20 characters in length.')

    while True:
        author = input('Author: ')
        if is_valid_author_name(author):
            break
        print('Invalid Author Name! Try Again!')
        print('Author name should contain only alphabets and be greater than 0 in length.')
        
    return parent_dir, name, author

def make_dir(parent_dir, name):
    '''Creates the project directory and return the path.'''
    
    path = os.path.join(parent_dir, name)
    os.mkdir(path)
    print(f'Created directory {path}')
    return path

def createREADME(parent_dir, name, author):
    '''creates README.md'''
    
    path = parent_dir+'\README.md'
    content = f"Welcome to {name}\nCreated by {author}"

    with open(path, 'w') as README:
        README.write(content)

    print(f'Created file {path}')

def createMain(parent_dir, name):
    '''creates main python file'''
    
    path = parent_dir+'\main.py'
    content = f"if __name__ == '__main__':\n\tprint('Welcome to {name}')"

    with open(path, 'w') as main_file:            
        main_file.write(content)
    
    print(f'Created file {path}')

def createTODO(parent_dir, name):
    '''creates TODO.md'''
    
    path = parent_dir+'\TODO.md'
    content = f'TODO for {name}'
    
    with open(path, 'w') as TODO:
        TODO.write(content)
        
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
