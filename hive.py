#!/usr/bin/python
import a,b,os,commands
def hive_setup():
	os.system("tar -xvzf /root/Desktop/apache-hive-0.13.1-bin.tar.gz")
	os.system("mv /root/Desktop/apache-hive-0.13.1-bin /hive")
	f=open("/root/.bashrc","r")
	f.write("# .bashrc\n\n# User specific aliases and functions\n\nalias rm='rm -i'\nalias cp='cp -i'\nalias mv='mv -i'\n# Source global definitions\nif [ -f /etc/bashrc ]; then\n        . /etc/bashrc\nfi\n\nexport PATH=/hive/bin/:$PATH\nexport HIVE_HOME=/hive/")
	f.close()
	return
def hive_execute(str1):
	os.system("echo -e "+str1+" | hive")
	return 
def give_hive_query():
	s=raw_input("Enter HIVEql query:")
	hive.hive_execute(s)
	return 
	


