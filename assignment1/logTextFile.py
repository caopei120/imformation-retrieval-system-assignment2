import os
import shutil
from assignment1.util import strip_path


def create_log(log_name):
    log_name = strip_path(log_name)
    is_exists = os.path.exists(log_name)
    if not is_exists:
        with open(log_name, encoding='utf-8', mode='a') as file:
            file.close()
        print(log_name + ' created successfully')
        return "success"
    else:
        print(log_name + ' file already exists')
        return "fail"


# log_name = '/home/test'
# createDir(log_name)

def delete_log(log_name):
    log_name = strip_path(log_name)
    is_exists = os.path.exists(log_name)
    if not is_exists:
        print(log_name + ' file does not exist')
        return "fail"
    else:
        os.remove(log_name)
    return "success"


def move_log(old_log_name, new_log_name):
    old_log_name = strip_path(old_log_name)
    if not os.path.exists(old_log_name):
        print(old_log_name + ' old file does not exist')
        return "fail"
    else:
        shutil.move(old_log_name, new_log_name)
    return "success"


# deleteDir(log_name)

def read_log(log_name):
    log_name = strip_path(log_name)
    is_exists = os.path.exists(log_name)
    if not is_exists:
        print(log_name + ' file does not exist')
        return "fail"
    with open(log_name, 'r') as file:
        content = file.read()
        file.close()
    return content


# read_log('/Users/cp/Documents/pythontest/a.txt')

def write_log(log_path, write_str):
    with open(log_path, encoding='utf-8', mode='a') as file:
        file.write(write_str + '\n')
        file.close()
    return "success"

# write_log('/Users/cp/Documents/pythontest/a.txt','hello world')
