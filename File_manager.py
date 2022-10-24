import os
import zipfile

with open(r'path.txt') as f:
    main_path = f.readline()

current_path = main_path
logged_in = False


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
            print(text.split('\n'))
            f2.writelines(text.split('\n'))
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


def sign_in(username, password):
    global logged_in
    if username not in os.listdir(main_path):
        create_folder(username)
        change_path('\\'+username)
        create_file('user_data.txt')
        write_into_file('user_data.txt', f'{username}\n{password}')
        log_in(username, password)
    else:
        print(f'\x1b[1;31mUser {username} already exists.\x1b[0m')


def log_in(username, password):
    global logged_in
    global main_path
    if username in os.listdir(main_path):
        with open(main_path+'\\'+username+'\\'+'user_data.txt', mode='r') as f:
            rdl = f.readlines()
            if rdl == [username+'\n', password]:
                change_path('\\'+username)
                main_path = main_path+'\\'+username
                logged_in = True
                print(f'\n\x1b[1;36mUser {username} logged in successfully.\x1b[0m')
            else:
                print(f'\x1b[1;31mIncorrect username or password.\x1b[0m')
    else:
        print(f'\x1b[1;31mUser {username} does not exist.\x1b[0m')


def space_control():
    size = os.path.getsize(main_path)
    max_size = 536870912
    if size < max_size:
        return True
    else:
        return False


def zip_file(filename):
    if filename in os.listdir(current_path):
        if filename.split('.')[0]+'.zip' not in os.listdir(current_path):
            with zipfile.ZipFile(current_path+'\\'+filename.split('.')[0]+'.zip', mode='w') as z:
                os.chdir(current_path)
                z.write(filename, compress_type=zipfile.ZIP_DEFLATED)
                delete_file(filename)
            print(f"\x1b[1;36mFile {filename.split('.')[0]+'.zip'} has been zipped.\x1b[0m")
        else:
            print(f"\x1b[1;31mFile {filename.split('.')[0]+'.zip'} already exists.\x1b[0m")
    else:
        print(f'\x1b[1;31mFile {filename} does not exist.\x1b[0m')


def unzip_file(filename):
    if filename.split('.')[1] == 'zip':
        if filename in os.listdir(current_path):
            with zipfile.ZipFile(current_path+'\\'+filename, mode='r') as z:
                z.extractall(current_path)
            delete_file(filename)
            print(f"\x1b[1;36mFile {filename} has been unzipped.\x1b[0m")
        else:
            print(f'\x1b[1;31mFile {filename} does not exist.\x1b[0m')
    else:
        print(f'\x1b[1;31mFile {filename} is not a zip file.\x1b[0m')


run = True


while run:
    if not logged_in:
        act = input('\x1b[1;36mInput a command: \x1b[0m')

        if act.lower() == 'quit':
            print('\x1b[1;31mQuit\x1b[0m')
            break

        if act.lower() == 'sign in':
            username = input('\x1b[1;36mInput a username: \x1b[0m')
            password = input('\x1b[1;36mInput a password: \x1b[0m')
            sign_in(username, password)

        elif act.lower() == 'log in':
            username = input('\x1b[1;36mInput a username: \x1b[0m')
            password = input('\x1b[1;36mInput a password: \x1b[0m')
            log_in(username, password)

        else:
            print(f'\x1b[1;31mUnknown command.\x1b[0m')

    else:
        visible_path = current_path.replace('\\'.join(main_path.split('\\')[:-1]), '', 1)
        print(f'\n\x1b[1;36mCurrent path: \x1b[1;32m{visible_path}\x1b[0m')

        if space_control():
            print(f'\n\x1b[1;36mSpace left: \x1b[1;32m{round((536870912 - os.path.getsize(main_path))/1048576, 5)}/512 MB\x1b[0m')
        else:
            print(f'\x1b[1;31mYou are out of space!\x1b[0m')
            break

        print(f'\x1b[1;36mAvailable files:\x1b[1;32m')
        for i in os.listdir(current_path):
            if i != 'user_data.txt' and os.listdir(current_path) != ['user_data.txt']:
                print(i)

        act = input('\x1b[1;36mInput a command: \x1b[0m')

        if act.lower() == 'quit':
            print('\x1b[1;31mQuit\x1b[0m')
            break

        elif main_path not in current_path:
            print('\x1b[1;31mYou cannot do anything there, you were moved to the main path.\x1b[0m')
            current_path = main_path
            continue

        elif act.lower() == 'create folder':
            filename = input('\x1b[1;36mInput a folder name: \x1b[0m')
            create_folder(name=filename)
            continue

        elif act.lower() == 'delete folder':
            filename = input('\x1b[1;36mInput a folder name: \x1b[0m')
            delete_folder(filename)
            continue

        elif act.lower() == 'change path':
            path = input('\x1b[1;36mWrite your path: \x1b[0m').replace('/', '\\')
            change_path(path)
            continue

        elif act.lower() == 'create file':
            filename = input('\x1b[1;36mInput a filename: \x1b[0m').replace('/', '\\')
            create_file(filename)
            continue

        elif act.lower() == 'write into file':
            filename = input('\x1b[1;36mInput a filename: \x1b[0m')
            t = input('\x1b[1;36mWrite your text: \x1b[0m')
            write_into_file(filename, t)
            continue

        elif act.lower() == 'read file':
            filename = input('\x1b[1;36mInput a filename: \x1b[0m')
            read_file(filename)
            continue

        elif act.lower() == 'delete file':
            filename = input('\x1b[1;36mInput a filename: \x1b[0m')
            delete_file(filename)
            continue

        elif act.lower() == 'copy file':
            filename = input('\x1b[1;36mInput a filename: \x1b[0m')
            path = input('\x1b[1;36mInput path: \x1b[0m').replace('/', '\\')
            copy_file(filename, path)
            continue

        elif act.lower() == 'move file':
            filename = input('\x1b[1;36mInput a filename: \x1b[0m')
            path = input('\x1b[1;36mInput path: \x1b[0m').replace('/', '\\')
            move_file(filename, path)
            continue

        elif act.lower() == 'rename file':
            filename = input('\x1b[1;36mInput a filename: \x1b[0m')
            new_filename = input('\x1b[1;36mInput a new filename: \x1b[0m')
            rename_file(filename, new_filename)
            continue

        elif act.lower() == 'zip file':
            filename = input('\x1b[1;36mInput a filename: \x1b[0m')
            zip_file(filename)

        elif act.lower() == 'unzip file':
            filename = input('\x1b[1;36mInput a filename: \x1b[0m')
            unzip_file(filename)

        else:
            print('\x1b[1;31mUnknown command\x1b[0m')
