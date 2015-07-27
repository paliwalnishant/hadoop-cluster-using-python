import os,time,commands,sys


os.system('dialog  --menu  "Create your Custom hadoop cluster"   75 75  5  1 "Check the current avaibility of nodes"      2   "Create Name-Node"   3  "Create Job-Tracker"  4  "Create data-node and task-tracker "  5  "Check the status of cluster" 6 " Exit"  2>/tmp/c.txt')


f=open("/tmp/c.txt",'r')
c=f.read()
f.close()

if c == '1' :
	os.system("python /root/Desktop/python/ip.py")

elif c == '2' :
	
	os.system("python /root/Desktop/python/namenode.py")

elif c == '3' :
	os.system("python /root/Desktop/python/jobtracker.py")

elif c == '4' :
	os.system("python /root/Desktop/python/datanode.py")

elif c == '5' :
	os.system("exit()")
else :
	print 'Please enter correct choice'
