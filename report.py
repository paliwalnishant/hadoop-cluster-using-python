#!/usr/bin/python


import os
import commands



f=open("/tmp/namenode.txt",'r')
nip=f.read()


os.system('sshpass -p redhat ssh -X %s firefox %s:50070 |python /root/Desktop/python/mnu1.py'%(nip,nip))
#os.system('python /root/Desktop/python/dfsadmin.py')
