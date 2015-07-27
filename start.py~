#!/usr/bin/python
import  os,time,commands,sys


os.system('dialog     --infobox  "Welcome to hadoop tool"   5  30')
time.sleep(2)
os.system('dialog  --msgbox  "Press okay to cont"  10  30')	
os.system('dialog  --inputbox  "Enter user name "   5  30  2>/tmp/u.txt')
os.system('dialog  --insecure --passwordbox  "Enter password "   10  30   2>/tmp/p.txt')
f=open('/tmp/u.txt','r')
u=f.read()
f.close()
f1=open('/tmp/p.txt','r')
p=f1.read()
f1.close()
if   u  ==  "root" and  p ==  "redhat" :
	os.system("python  /root/Desktop/python/mnu.py")
else :
	print  "check ur login details "


     
