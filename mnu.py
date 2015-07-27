#!/usr/bin/python


import os,time,commands,sys,ipin


os.system('dialog  --menu  "Select your choice"   75 75  5  1 "Check the current avaibility of nodes"      2   "Create your own custom Hadoop Cluster"   3  "Create a hadoop cluster on one click"  4  "Do you want any help "  5  "Exit"  2>/tmp/b.txt')


f=open("/tmp/b.txt",'r')
c=f.read()
f.close()

if c == '1' :
	os.system("python /root/Desktop/python/ip.py")

elif c == '2' :
	
	os.system("python /root/Desktop/python/mnu1.py")

elif c == '3' :
	os.system("python /root/Desktop/python/typicalf.py")

elif c == '4' :
	print 'Coming soon'

elif c == '5' :
	os.system("exit()")
else :
	print 'Please enter correct choice'


