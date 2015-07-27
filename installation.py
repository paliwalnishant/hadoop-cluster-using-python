#!/usr/bin/python2
import commands
import os


#install jdk
def install_jdk() :

	os.system("yum install jdk -y ")



#install hadoop
def install_hadoop() :

	os.system("yum install hadoop -y")
