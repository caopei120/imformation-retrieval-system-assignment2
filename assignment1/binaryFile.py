import os
import shutil
from assignment1.util import strip_path


def create_file(file_name):
    file_name = strip_path(file_name)
    is_exists = os.path.exists(file_name)
    if not is_exists:
        with open(file_name, mode='wb') as file:
            file.write(bytes('hello binary', 'ascii'))
            file.close()
        print(file_name + ' created successfully')
        return "success"
    else:
        print(file_name + ' file already exists')
        return "fail"


# file_name = 'D:\home\\test'
# createDir(file_name)

def delete_file(file_name):
    file_name = strip_path(file_name)
    is_exists = os.path.exists(file_name)
    if not is_exists:
        print(file_name + ' file does not exist')
        return "fail"
    else:
        os.remove(file_name)
    return "success"


# deleteDir(file_name)

def move_file(old_file_name, new_file_name):
    old_file_name = strip_path(old_file_name)
    if not os.path.exists(old_file_name):
        print(old_file_name + ' old file does not exist')
        return "fail"
    else:
        shutil.move(old_file_name, new_file_name)
    return "success"


def update_file(file_name, content):
    file_name = strip_path(file_name)
    is_exists = os.path.exists(file_name)
    if is_exists:
        with open(file_name, mode='wb') as file:
            file.write(bytes(content, 'ascii'))
            file.close()
        print(file_name + ' update successfully')
        return "success"
    else:
        print(file_name + ' file not exists')
        return "fail"


def read_file(file_name):
    file_name = strip_path(file_name)
    is_exists = os.path.exists(file_name)
    if not is_exists:
        print(file_name + ' file does not exist')
        return "fail"
    with open(file_name, 'rb') as file:
        file_content = file.read()
        file.close()
    return file_content

# read_file('/Users/cp/Documents/pythontest/b.png')
