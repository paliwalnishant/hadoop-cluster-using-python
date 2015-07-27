#!/usr/bin/python2

import os,commands


os.system('dialog  --inputbox  "Enter jobtracker ip :"   5  30  2>/tmp/jobtracker.txt')

def jobtracker():
	f1=open("/tmp/jobtracker.txt",'r')
	j_ip=f1.read()
	f1.close()
	
	f1=open("/tmp/namenode.txt",'r')
	n_ip=f1.read()
	f1.close()

	
	f1=open("/root/Desktop/nfiles/jtcore.py",'w+')
	f1.write("""#!/usr/bin/python2
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
	f1.close()

	#Job-tracker mapred-site.xml 

	f1=open("/root/Desktop/nfiles/jtmapred.py",'w+')
	f1.write("""#!/usr/bin/python2
f=open("/etc/hadoop/mapred-site.xml",'w')
f.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>"""+j_ip+""":9002</value>
</property>
</configuration>''')
f.close()
	""")
	f1.close()

	#Starting jobtracker

	os.system("sshpass -p redhat scp {/root/Desktop/nfiles/jtmapred.py,/root/Desktop/nfiles/jtcore.py} %s:/root/Desktop" %j_ip)
	#os.system("sshpass -p redhat scp /root/Desktop/nfiles/jtcore.py"+j_ip+":/root/Desktop")
	os.system("sshpass -p redhat ssh %s python /root/Desktop/jtmapred.py" %j_ip)
	os.system("sshpass -p redhat ssh %s python /root/Desktop/jtcore.py" %j_ip)
	os.system("sshpass -p redhat ssh %s hadoop-daemon.sh start jobtracker" %j_ip )
	os.system("sshpass -p redhat ssh %s /usr/java/jdk1.7.0_51/bin/jps" %j_ip )





jobtracker()
