def  datanodeip():
	n=raw_input('Enter the no. of datanodes you want')
	h=int(n)	
	count=0
	f=[]
	for count in range(0,h) :
		j=raw_input('Enter IP of %s datanode '%count)
		f.append(j)
	print f	
	

	'''
	t=[]
	for i  in f  :
					
		temp = threading.Thread(target=lw,args=(i,))
		temp.start()
		t.append(temp)
	for i in t :
		i.join()

	'''



def jobtrackerip():
	n=raw_input("Enter the ip of jobtracker")
	


#os.system('dialog  --inputbox  "Enter namenode ip :"   5  30  2>/tmp/namenode.txt')
