#!/usr/bin/python





import os
import commands
import operator
commands.getstatusoutput("nmap -sL '192.168.1.0/24' | cut -d" " -f6 |cut -d'(' -f2 | cut -d')' -f1 > ip.txt")

f1=open("/root/Desktop/python/ip.txt",'r+')
ipno=f1.readlines()#Stripping to be done

for i in range(0,len(ipno)):
	ipno[i]=ipno[i][:-1]
f1.close()

n=len(ipno)
ramval2=[]
storageval2=[]

for x in range(0,n):
	
		ramval=commands.getoutput("sshpass -p 'redhat' ssh "+ ipno[x]+" free -m | awk -F' ' '{print $3}' | head -2 | tail -1 ")
		ramval2.append(ramval)

		
		storageval=commands.getoutput("sshpass -p 'redhat' ssh "+ ipno[x]+" df  | awk -F' ' '{print $4}' | head -3 | tail -1")
		storageval2.append(storageval)		

ramips={}

i=0
while i != len(ipno):	
	ramips.update({ipno[i]:ramval2[i]})
	i=i+1
sramips=sorted( ramips.items(), key=operator.itemgetter(1))



storageips={}

i=0
while i != len(ipno):	
	storageips.update({ipno[i]:storageval2[i]})
	i=i+1
sstorageips=sorted( storageips.items(), key=operator.itemgetter(1))


namenode=sstorageips[0][0]
jobtracker=sramips[-1][0]


print namenode 
print jobtracker
print sramips
print sstorageips

#Creating namenode


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


f9=open("/root/Desktop/test/hdfs-site.xml","w+")
f9.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/nnf</value>
</property>
</configuration>""");
f9.close()

os.system("sshpass -p redhat scp  /root/Desktop/test/core-site.xml "+namenode+":/etc/hadoop")
os.system("sshpass -p redhat scp  /root/Desktop/test/hdfs-site.xml "+namenode+":/etc/hadoop")
os.system("sshpass -p redhat ssh "+namenode+" hadoop namenode -format -Y")
os.system("sshpass -p redhat ssh "+namenode+" hadoop-daemon.sh stop namenode")
os.system("sshpass -p redhat ssh "+namenode+" hadoop-daemon.sh start namenode")
confirmnamen=commands.getoutput("sshpass -p redhat ssh "+namenode+" /usr/java/jdk1.7.0_51/bin/jps|awk -F' ' '{print $2}'|head -2")
print confirmnamen



#creating jobtracker


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


f9=open("/root/Desktop/test/mapred-site.xml","w+")
f9.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>"""+jobtracker+""":9002</value>
</property>
</configuration>""");
f9.close()

commands.getoutput("sshpass -p redhat scp  /root/Desktop/test/core-site.xml "+jobtracker+":/etc/hadoop")
commands.getoutput("sshpass -p redhat scp  /root/Desktop/test/mapred-site.xml "+jobtracker+":/etc/hadoop")
commands.getoutput("sshpass -p redhat ssh "+jobtracker+" hadoop-daemon.sh stop jobtracker")
commands.getoutput("sshpass -p redhat ssh "+jobtracker+" hadoop-daemon.sh start jobtracker")
confirmnamen=commands.getoutput("sshpass -p redhat ssh "+jobtracker+" /usr/java/jdk1.7.0_51/bin/jps|awk -F' ' '{print $2}'|head -2")
print confirmnamen



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
	<value>hdfs://"""+namenode+""":9001</value>
	</property>
	</configuration>""");
	f8.close()


	f9=open("/root/Desktop/test/hdfs-site.xml","w+")
	f9.write("""<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

	<!-- Put site-specific property overrides in this file. -->

	<configuration>
	<property>
	<name>dfs.data.dir</name>
	<value>/ddf</value>
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
	<value>hdfs://"""+jobtracker+""":9001</value>
	</property>
	</configuration>""");
	f6.close()

	commands.getoutput("sshpass -p redhat scp  /root/Desktop/test/core-site.xml "+datanode+":/etc/hadoop")
	commands.getoutput("sshpass -p redhat scp  /root/Desktop/test/hdfs-site.xml "+datanode+":/etc/hadoop")
	commands.getoutput("sshpass -p redhat scp  /root/Desktop/test/mapred-site.xml "+datanode+":/etc/hadoop")
	commands.getoutput("sshpass -p redhat ssh "+datanode+" hadoop-daemon.sh stop datanode")
	commands.getoutput("sshpass -p redhat ssh "+datanode+" hadoop-daemon.sh start datanode")		
	commands.getoutput("sshpass -p redhat ssh "+datanode+" hadoop-daemon.sh stop tasktracker")
	commands.getoutput("sshpass -p redhat ssh "+datanode+" hadoop-daemon.sh start tasktracker")
	confirmnamen=commands.getoutput("sshpass -p redhat ssh "+datanode+" /usr/java/jdk1.7.0_51/bin/jps|awk -F' ' '{print $2}'|head -2")
	print confirmnamen


for i in range(1,len(sramips)):
	
	datan=sramips[i][0]
	print datan
	datanode(datan,namenode,jobtracker)

