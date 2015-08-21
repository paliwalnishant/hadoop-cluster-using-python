#!/usr/bin/python2

#!/usr/bin/python
import commands
import thread
import os 


#x=commands.getoutput("nmap -sP 192.168.1.0/24 | grep 192 | awk -F ' ' '{print $6}' | awk -F '(' '{print $2}' | awk -F')' '{print $1}' >ip.txt ")

f=open("ip.txt",'r')
x=f.readlines()
for i in range(0,len(x)):
	x[i]=x[i][:-1]
f.close()



s=1
f=open("/root/Desktop/python/newip.txt","w+")
f.write("Sno""\t""ipno.""\t\t""Free RAM""\t\t""Free Space \n")
for i in x :
	ram=commands.getoutput("sshpass -p redhat ssh %s free -m| grep Mem | awk '{print $4}'"%i)
	disk=commands.getoutput("sshpass -p redhat ssh %s df --total -h | grep total | awk '{print $4}'"%i)	
	f.write("%d""\t"" %s""\t\t""%s""\t\t""%s\n"%(s,i,ram,disk))
	s+=1
	
f.close()


os.system('dialog --textbox /root/Desktop/python/newip.txt 50 100')




