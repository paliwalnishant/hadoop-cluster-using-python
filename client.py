#/usr/bin/python

import commands 
import os


os.system('dialog  --inputbox  "Enter client ip :"   5  30  2>/tmp/client.txt')
f1=open("/tmp/namenode.txt",'r')
namenode=f1.read()
f1.close()

#Name node core-site.xml

f8=open("/root/Desktop/test/core-site.xml","w+")
f8.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://"""+namenode+""":9001</value>
</property>
</configuration>""");
f8.close()


f=open("/tmp/client.txt",'r')
client=f.read()
f.close()


os.system("sshpass -p redhat scp  /root/Desktop/test/core-site.xml "+client+":/etc/hadoop")

	
	




