#!/usr/bin/python



import os 

os.system('dialog  --inputbox  "Enter the word which you want to count :" 75 75  2>/tmp/wcount.txt')
os.system('dialog  --inputbox  "Enter the path of file on hdfs system :"   50 50  2>/tmp/location.txt')

f1=open("/tmp/client.txt",'r')
client=f1.read()
f1.close()

f1=open("/tmp/wcount.txt",'r')
word=f1.read()
f1.close()

f1=open("/tmp/location.txt",'r')
location=f1.read()
f1.close()

os.system("sshpass -p redhat ssh %s hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar wordcount /%s /output123"%(client,location))


os.system("python /root/Desktop/python/clientmnu.py")
