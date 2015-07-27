#/usr/bin/python

import commands 
import os


os.system('dialog  --inputbox  "Enter namenode ip :"   5  30  2>/tmp/namenode.txt')


def namenode():

	f1=open("/tmp/namenode.txt",'r')
	n_ip=f1.read()
	f1.close()

	#Name node hdfs-site.xml
	f1=open("/root/Desktop/nfiles/nnhdfs.py",'w+')
	f1.write("""#!/usr/bin/python2
f=open("/etc/hadoop/hdfs-site.xml",'w')	
f.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/nnn1</value>
</property>
</configuration>''')
f.close()
	""")
	f1.close()

	#Name node core-site.xml 

	f2=open("/root/Desktop/nfiles/nncore.py",'w+')
	f2.write("""#!/usr/bin/python2
f=open("/etc/hadoop/core-site.xml",'w')
f.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://"""+n_ip+""":9001</value>
</property>
</configuration>''')
f.close()
	""")
	f2.close()



	#Starting name node

	commands.getstatusoutput("sshpass -p redhat scp {/root/Desktop/nfiles/nnhdfs.py,/root/Desktop/nfiles/nncore.py} %s:/root/Desktop"%n_ip)
	os.system("sshpass -p redhat ssh %s python /root/Desktop/nnhdfs.py" %n_ip)
	os.system("sshpass -p redhat ssh %s python /root/Desktop/nncore.py" %n_ip)
	os.system("sshpass -p redhat ssh %s hadoop namenode -format" %n_ip )
	os.system("sshpass -p redhat ssh %s hadoop-daemon.sh start namenode" %n_ip )
	os.system("sshpass -p redhat ssh %s /usr/java/jdk1.7.0_51/bin/jps" %n_ip )
 
	



namenode()
