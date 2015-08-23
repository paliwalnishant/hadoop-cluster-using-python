#!/usr/bin/python


import os
import commands


os.system('dialog  --inputbox  "Create a directory on hadoop cluster"   30  30  2>/tmp/dir.txt')
os.system('dialog  --msgbox  "Press okay to cont"  30  30')


f=open("/tmp/dir.txt",'r')
path=f.read()
f.close()

f=open("/tmp/client.txt",'r')
client=f.read()
f.close

os.system('sshpass -p redhat ssh %s hadoop fs -mkdir /%s '%(client,path))

os.system('python /root/Desktop/python/clientmnu.py')
