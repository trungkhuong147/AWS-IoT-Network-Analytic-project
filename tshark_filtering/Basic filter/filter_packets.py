def output (newfilename,oldfilename,listfile) :
	open(newfilename,'w').writelines([ line for line in open(oldfilename) if ('ICMP')  in line])
	open(newfilename,'a').writelines([ line for line in open(oldfilename) if ('TCP')  in line])



def filter() :
	L1=[]

	file1='botnetpcap.txt'
	
	f1filter="botnetpcap_filtered.txt"
	
	print ('called filter function in filter_packets.py')
	
	
	output (f1filter,file1,L1)	
	
