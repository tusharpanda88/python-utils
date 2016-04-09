
import os

def creat_file(path):
    for i in range(26):
        n = str(i).zfill(4)
        sub_path = path + n
        os.mkdir(sub_path)
    return path

if __name__ == '__main__':
    path = raw_input("enter path: ")
    creat_file(path)
