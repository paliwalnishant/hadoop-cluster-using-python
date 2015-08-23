import os,time,commands,sys


os.system('dialog  --menu  "Welcome to hadoop client portal"   75 75  7  1 "Create a client" 2 "Browse the hadoop cluster"     3   "Create a hadoop directory"   4  "Upload a file on hadoop cluster"  5  "Remove a file from the system "  6 "Count the number of words in the file" 7 "Back" 2>/tmp/c.txt')


f=open("/tmp/c.txt",'r')
c=f.read()
f.close()

if c == '1' :
	os.system("python /root/Desktop/python/client.py")
	os.system("python /root/Desktop/python/clientmnu.py")
		

elif c == '2' :
	
	os.system("python /root/Desktop/python/creport.py")

elif c == '3' :
	os.system("python /root/Desktop/python/mkdir.py")

elif c == '4' :
	os.system("python /root/Desktop/python/uploadfile.py")



elif c == '5' :

	os.system("python /root/Desktop/python/removefile.py")

elif c == '7' :
	os.system("python /root/Desktop/python/mnu.py")

elif c == '6' :
	os.system("python /root/Desktop/python/jobrun.py")

else :
	print 'Please enter correct choice'
