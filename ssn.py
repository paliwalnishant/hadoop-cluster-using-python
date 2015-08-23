#/usr/bin/python

import commands 
import os


os.system('dialog  --inputbox  "Enter Secondary namenode ip :"   5  30  2>/tmp/ssn.txt')
f1=open("/tmp/ssn.txt",'r')
ssn=f1.read()
f1.close()

f1=open("/tmp/namenode.txt",'r')
namenode=f1.read()
f1.close()


#Name node hdfs-site.xml

f8=open("/root/Desktop/test/ssn/core-site.xml","w+")
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


f9=open("/root/Desktop/test/ssn/hdfs-site.xml","w+")
f9.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.http.address</name>
<value>"+namenode+":50070</value>
</property>

<property>
<name>dfs.secondary.http.address</name>
<value>"+ssn+":50090</value>
</property>

<property>
<name>fs.checkpoint.dir</name>
<value>/check</value>
</property>

<property>
<name>fs.checkpoint.edits.dir</name>
<value>/old</value>
</property>
</configuration>""");
f9.close()

os.system("sshpass -p redhat scp  /root/Desktop/test/ssn/core-site.xml "+ssn+":/etc/hadoop")
os.system("sshpass -p redhat scp  /root/Desktop/test/ssn/hdfs-site.xml "+ssn+":/etc/hadoop")
#os.system("sshpass -p redhat ssh "+namenode+" hadoop namenode -format -Y >/tmp/null")
os.system("sshpass -p redhat ssh "+ssn+" hadoop-daemon.sh stop secondarynamenode ")
os.system("sshpass -p redhat ssh "+ssn+" hadoop-daemon.sh start secondarynamenode ")
confirmnamen=commands.getoutput("sshpass -p redhat ssh "+ssn+" /usr/java/jdk1.7.0_51/bin/jps|awk -F' ' '{print $2}'|head -2")
print confirmnamen
	
	




################################################################
