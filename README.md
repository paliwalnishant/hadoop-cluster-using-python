# hadoop-cluster-using-python

#Tool can be used for Configuration of multinode hadoop cluster on one click .
 python TUI has been used 

Project includes implementation of :-

##1. Distributed Storage - Name Node , Data Node , Secondary Name node 

##2. Distributed Computing - Map Reduce , Job tracker , Task tracker 

##3. Quota Set - Quota can be set on directory for file size and the number on files which cab be uploaded on cluster.

##4. Secondary Namenode - For checkpointing 

##5 Typical Cluster configuration- In this type of configuration nodes are decided according to their specification. eg. Node with more space created as Data node. Node with more free Ram created as task tracker.

##6 Custom Cluster configuration - A list showing the all ip addresses available with their storage and Ram capacity will be provided so that you can decide on your own and create.


How to use tool :-


1.Install hadoop version 1 on Redhat linux 6 or above  

2.Create a folder named python and test on your Desktop.

3.Now Run start.py



Future aspects of the project :-

Currently i am working on shifting the project from python TUI to CGI . 

A web portal can be created through which any user can create and access hadoop cluster from anywhere .

A better user interface with the help of HTML, CSS, PHP can be created which through which multi node cluster can easily be created. 



