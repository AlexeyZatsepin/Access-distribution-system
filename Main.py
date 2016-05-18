#!/usr/bin/env python
# coding=utf-8
from Session import main
from utils import count_in_base,count_in_file
from hashlib import sha512
import os

if not os.path.exists(os.getcwd() + "/config.txt"):
    info = sha512(os.getcwd())
    with open('config.txt', 'a') as handle:
        ifile = info.hexdigest()
        handle.write(ifile)
if __name__ == '__main__':
    with open('config.txt', 'rw') as config:
        data = config.read()
        info = sha512(os.getcwd())
        hash = info.hexdigest()
        if data == hash:
            if count_in_base()>count_in_file():
                #print(count_in_base())
                #print(count_in_file())
                print("Error: you create fraud user in db")
            else:
                main()
        else:
            print "Not Verified"
