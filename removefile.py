#!/usr/bin/python


import os
import commands


os.system('dialog  --inputbox  "Enter file path"   5  30  2>/tmp/rmrpath.txt')
os.system('dialog  --msgbox  "Press okay to cont"  10  30')


f=open("/tmp/rmrpath.txt",'r')
path=f.read()
f.close()

f=open("/tmp/client.txt",'r')
client=f.read()
f.close

os.system('sshpass -p redhat ssh %s hadoop fs -rmr /%s'%(client,path))
os.system('python /root/Desktop/python/clientmnu.py')

