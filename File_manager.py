import os

with open(r'path.txt') as f:
    main_path = f.readline()

current_path = main_path


def get_cur_path():
    os.getcwd()


def create_folder(path=current_path, name='New folder'):
    if name not in os.listdir(current_path):
        os.mkdir(path+'\\'+name)
    else:
        print(f'\x1b[1;31mFolder named {name} already exists.\x1b[0m')


def delete_folder(name):
    if name in os.listdir(current_path):
        try:
            os.rmdir(current_path+'\\'+name)
        except:
            print(f'\x1b[1;31mFolder {name} is not empty.\x1b[0m')
    else:
        print(f'\x1b[1;31mFolder {name} does not exist.\x1b[0m')


def change_path(path):
    global current_path
    if path == '..\\':
        current_path = '\\'.join(current_path.split('\\')[:-1])
    elif path == '\\':
        current_path = main_path
    else:
        current_path = main_path+path


def create_file(name):
    if name not in os.listdir(current_path):
        with open(current_path+'\\'+name, mode='w') as f1:
            pass
    else:
        print(f'\x1b[1;31mFile {name} already exists.\x1b[0m')


def write_into_file(name, text, repl=False):
    if name+'.txt' in os.listdir(current_path):
        if not repl:
            with open(current_path+'\\'+name+'.txt', mode='a') as f2:
                f2.write(text)
        else:
            with open(name+'.txt', mode='w') as f2:
                f2.write(text)
    else:
        print(f'\x1b[1;31mFile named {name}.txt does not exist.\x1b[0m')


run = True

while run:
    print(f'\x1b[1;32mCurrent path: {current_path}\x1b[0m')
    act = input('\x1b[1;36mType what you want to do: \x1b[0m')

    if act.lower() == 'quit':
        print('\x1b[1;31mQuit\x1b[0m')
        break

    if main_path not in current_path:
        print('\x1b[1;31mYou cannot do anything there, you were moved to the main path.\x1b[0m')
        current_path = main_path
        continue

    if act.lower() == 'create folder':
        filename = input('Write a name for the folder: ')
        create_folder(name=filename)
        continue

    if act.lower() == 'delete folder':
        filename = input('Write a name for the directory: ')
        delete_folder(filename)
        continue

    if act.lower() == 'change path':
        path = input('Write your path: ').replace('/', '\\')
        change_path(path)
        continue

    if act.lower() == 'create file':
        filename = input('\x1b[1;36mWrite a filename: \x1b[0m').replace('/', '\\')
        create_file(filename)
        continue

    if act.lower() == 'write into file':
        filename = input('\x1b[1;36mWrite a filename: \x1b[0m')
        r = input('x1b[1;36mDo you want to replace the content?\x1b[0m')
        t = input('x1b[1;36mWrite your text: \x1b[0m')
        if r.lower() == 'true':
            write_into_file(filename, t, True)
        else:
            write_into_file(filename, t)

    else:
        print('\x1b[1;31mUnknown command\x1b[0m')
