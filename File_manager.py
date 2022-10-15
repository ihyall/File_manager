import os

with open(r'path.txt') as f:
    main_path = f.readline()

current_path = main_path


def get_cur_path():
    os.getcwd()


def create_folder(name='New folder'):
    if name not in os.listdir(current_path):
        os.mkdir(current_path+'\\'+name)
        print(f'\x1b[1;36mFolder {name} has been created.\x1b[0m')
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
        if os.access(main_path+path, mode=os.F_OK):
            current_path = main_path + path
        else:
            print(f'\x1b[1;31mPath {current_path} does not exist, you were moved to the main path.\x1b[0m')
            current_path = main_path
            return False
    return True


def create_file(name):
    if name not in os.listdir(current_path):
        with open(current_path+'\\'+name, mode='w') as f1:
            pass
        print(f'\x1b[1;36mFile {name} has been created.\x1b[0m')
    else:
        print(f'\x1b[1;31mFile {name} already exists.\x1b[0m')


def write_into_file(name, text):
    if name in os.listdir(current_path):
        with open(current_path+'\\'+name, mode='w') as f2:
            f2.write(text)
    else:
        print(f'\x1b[1;31mFile {name} does not exist.\x1b[0m')


def read_file(name):
    if name in os.listdir(current_path):
        with open(current_path+'\\'+name, mode='r') as f:
            a = f.readlines()
            print('\x1b[1;36mFile content: \x1b[0m')
            print(''.join(a))
    else:
        print(f'\x1b[1;31mFile {name} does not exist.\x1b[0m')


def delete_file(name):
    if name in os.listdir(current_path):
        os.remove(current_path+'\\'+name)
        print(f'\x1b[1;36mFile {name} has been deleted.\x1b[0m')
    else:
        print(f'\x1b[1;31mFile {name} does not exist.\x1b[0m')


def copy_file(name, path):
    if name in os.listdir(current_path):
        if os.access(mode=os.F_OK):
            if name not in os.listdir(main_path+path):
                with open(current_path+'\\'+name, mode='r') as f:
                    a = f.readlines()
                    change_path(path)
                    with open(current_path + '\\' + name, mode='w') as f1:
                        f1.writelines(a)
                print(f'\x1b[1;36mFile {name} was copied to {path}.\x1b[0m')
            else:
                print(f'\x1b[1;31mFile {name} already exists in {path}.\x1b[0m')
        else:
            print(f'\x1b[1;31mPath {path} is incorrect.\x1b[0m')
    else:
        print(f'\x1b[1;31mFile {name} does not exist.\x1b[0m')


def move_file(name, path):
    old_path = current_path+'\\'+name
    if os.access(main_path+path, mode=os.F_OK):
        if name in os.listdir(current_path):
            if name not in os.listdir(main_path+path):
                with open(current_path+'\\'+name, mode='r') as f:
                    a = f.readlines()
                    change_path(path)
                    with open(current_path + '\\' + name, mode='w') as f1:
                        f1.writelines(a)
                os.remove(old_path)
                print(f'\x1b[1;36mFile {name} was moved to {path}.\x1b[0m')
            else:
                print(f'\x1b[1;31mFile {name} already exists in {path}.\x1b[0m')
        else:
            print(f'\x1b[1;31mFile {name} does not exist.\x1b[0m')
    else:
        print(f'\x1b[1;31mPath {path} is incorrect.\x1b[0m')


def rename_file(name, new_name):
    if name in os.listdir(current_path):
        if new_name not in os.listdir(current_path):
            os.rename(current_path+'\\'+name, current_path+'\\'+new_name)
        else:
            print(f'\x1b[1;31mFile {new_name} already exists.\x1b[0m')
    else:
        print(f'\x1b[1;31mFile {name} does not exist.\x1b[0m')

run = True

while run:
    visible_path = current_path.replace('\\'.join(main_path.split('\\')[:-1]), '', 1)
    print(f'\n\x1b[1;36mCurrent path: \x1b[1;32m{visible_path}\x1b[0m')
    print(f'\x1b[1;36mAvailable files:\x1b[1;32m')
    for i in os.listdir(current_path):
        print(i)
    act = input('\x1b[1;36mInput a command: \x1b[0m')

    if act.lower() == 'quit':
        print('\x1b[1;31mQuit\x1b[0m')
        break

    if main_path not in current_path:
        print('\x1b[1;31mYou cannot do anything there, you were moved to the main path.\x1b[0m')
        current_path = main_path
        continue

    if act.lower() == 'create folder':
        filename = input('\x1b[1;36mInput a folder name: \x1b[0m')
        create_folder(name=filename)
        continue

    if act.lower() == 'delete folder':
        filename = input('\x1b[1;36mInput a folder name: \x1b[0m')
        delete_folder(filename)
        continue

    if act.lower() == 'change path':
        path = input('\x1b[1;36mWrite your path: \x1b[0m').replace('/', '\\')
        change_path(path)
        continue

    if act.lower() == 'create file':
        filename = input('\x1b[1;36mInput a filename: \x1b[0m').replace('/', '\\')
        create_file(filename)
        continue

    if act.lower() == 'write into file':
        filename = input('\x1b[1;36mInput a filename: \x1b[0m')
        t = input('\x1b[1;36mWrite your text: \x1b[0m')
        write_into_file(filename, t)
        continue

    if act.lower() == 'read file':
        filename = input('\x1b[1;36mInput a filename: \x1b[0m')
        read_file(filename)
        continue

    if act.lower() == 'delete file':
        filename = input('\x1b[1;36mInput a filename: \x1b[0m')
        delete_file(filename)
        continue

    if act.lower() == 'copy file':
        filename = input('\x1b[1;36mInput a filename: \x1b[0m')
        path = input('\x1b[1;36mInput path: \x1b[0m').replace('/', '\\')
        copy_file(filename, path)
        continue

    if act.lower() == 'move file':
        filename = input('\x1b[1;36mInput a filename: \x1b[0m')
        path = input('\x1b[1;36mInput path: \x1b[0m').replace('/', '\\')
        move_file(filename, path)
        continue

    if act.lower() == 'rename file':
        filename = input('\x1b[1;36mInput a filename: \x1b[0m')
        new_filename = input('\x1b[1;36mInput a new filename: \x1b[0m')
        rename_file(filename, new_filename)
        continue

    else:
        print('\x1b[1;31mUnknown command\x1b[0m')
