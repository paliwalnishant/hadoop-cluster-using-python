#!/usr/bin/python

import os,commands


os.system('dialog  --inputbox  "How many datanodes do you need :"   30  30  2>/tmp/countdatanode.txt')
f1=open("/tmp/countdatanode.txt",'r')
c=f1.read()
f1.close()
h=int(c)

for i in range(0,h):
	
	os.system('dialog  --inputbox  "Enter ip of datnode :"  30 30  2>/tmp/datanodeip%d.txt'%i)
	





def datanode(dd,nn,jt):

	datanode=dd
	namenode=nn
	jobtracker=jt


	#creating a data node and task-tracker



	f8=open("/root/Desktop/test/core-site.xml","w+")
	f8.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://%s:9001</value>
</property>
</configuration>"""
	%namenode);
	f8.close()


	f9=open("/root/Desktop/test/datah/hdfs-site.xml","w+")
	f9.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/ddd</value>
</property>
</configuration>""");
	f9.close()



	f6=open("/root/Desktop/test/mapred-site.xml","w+")
	f6.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>%s:9002</value>
</property>
</configuration>"""
	%jobtracker);
	f6.close()

	commands.getoutput("sshpass -p redhat scp  /root/Desktop/test/core-site.xml "+datanode+":/etc/hadoop")
	commands.getoutput("sshpass -p redhat scp  /root/Desktop/test/datah/hdfs-site.xml "+datanode+":/etc/hadoop")
	commands.getoutput("sshpass -p redhat scp  /root/Desktop/test/mapred-site.xml "+datanode+":/etc/hadoop")
	commands.getoutput("sshpass -p redhat ssh "+datanode+" hadoop-daemon.sh stop datanode >/tmp/null")
	commands.getoutput("sshpass -p redhat ssh "+datanode+" hadoop-daemon.sh start datanode >/tmp/null")		
	commands.getoutput("sshpass -p redhat ssh "+datanode+" hadoop-daemon.sh stop tasktracker >/tmp/null")
	commands.getoutput("sshpass -p redhat ssh "+datanode+" hadoop-daemon.sh start tasktracker >/tmp/null")
	#confirmnamen=commands.getoutput("sshpass -p redhat ssh "+datanode+" /usr/java/jdk1.7.0_51/bin/jps|awk -F' ' '{print $2}'|head -2")
	#print confirmnamen
		


f1=open("/tmp/countdatanode.txt",'r')
c=f1.read()
f1.close()
h=int(c)
#print h

for i in range(0,h):
	f1=open("/tmp/datanodeip%d.txt"%i,'r')
	dip=f1.read()
	#print dip

	f2=open("/tmp/namenode.txt",'r')
	nip=f2.read()
	f2.close()
	#print nip
	f3=open("/tmp/jobtracker.txt",'r')
	jip=f3.read()	
	f3.close()
	#print jip
	datanode(dip,nip,jip)
	
f1.close	



