#!/usr/bin/env python
# coding=utf-8
from Session import main
from hashlib import sha512
import os

#if not os.path.exists(os.getcwd()+"/config.txt"):
#    uname=''.join(os.uname())
#    info = sha512(os.getlogin() + uname + os.getcwd())
#    handle = open('config.txt', 'a')
#    afile=info.hexdigest()
#    handle.write(afile)
#    handle.close()
#else:
if __name__=='__main__':
    with open('config.txt', 'rw') as config:
        data = config.read()
        uname=''.join(os.uname())
        info = sha512(os.getlogin() + uname + os.getcwd())
        hash=info.hexdigest()
        if data==hash:
            main()
        else:
            print "Not Verified"
