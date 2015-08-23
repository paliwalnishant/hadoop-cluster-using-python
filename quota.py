#!/usr/bin/python


import os 


os.system('dialog  --inputbox  "Enter the directory on which you want to set quota :"   30  30  2>/tmp/quota.txt')
os.system('dialog  --menu  "Create your Custom hadoop cluster"   75 75  3  1 "Set quota on size"      2   "Set quota on files" 3 "Back" 2>/tmp/d.txt')

f=open("/tmp/d.txt",'r')
c=f.read()
f.close()

f=open("/tmp/quota.txt",'r')
quota=f.read()
f.close()


f=open("/tmp/namenode.txt",'r')
namenode=f.read()
f.close()




if c == '1' :
	os.system('dialog  --inputbox  "Enter the size :"   30  30  2>/tmp/size.txt')
	f=open("/tmp/size.txt",'r')
	size=int(f.read())
	f.close()
	os.system("sshpass -p redhat ssh %s hadoop dfsadmin -setSpaceQuota %d /%s"%(namenode,size,quota))
	os.system("python /root/Desktop/python/mnu.py")
elif c== '2' :
	os.system('dialog  --inputbox  "Enter the number of files :"   30  30  2>/tmp/size.txt')
	f=open("/tmp/size.txt",'r')
	size=int(f.read())
	f.close()
	os.system("sshpass -p redhat ssh %s hadoop dfsadmin -setQuota %d /%s"%(namenode,size,quota))
	os.system("python /root/Desktop/python/mnu.py")
elif c== '3' :
	os.system("python /root/Desktop/python/mnu.py")
else :
	print 'Please enter correct choice'	
