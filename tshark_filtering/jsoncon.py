# Python program to convert text 
# file to JSON 
import json 

# the file to be converted 
filename = 'botnetpcap_filtered.txt'

# fields in the sample file 
fields =['No', 'Time_Date', 'Time_Hours', 'SourceIP', 'DestinationIP', 'Protocol', 'Length', 'Info', 'Info_cont1', 'Info_cont2', 'Info_cont3','Info_cont4','Info_cont5','Info_cont6','Info_cont7'] 

with open(filename) as fh: 
	for line in fh: 	
		# reading line by line from the text file 
		description = list( line.strip().split(None, 15)) 
		# for output see below 
		print(description) 
		# for automatic creation of id for each packet 
		#sno ='packet id:'+str(l) 

		# loop variable 
		i = 0
		# intermediate dictionary 
		dict2 = {} 
		while i<len(fields): 
				
				if len(description) <= len(fields):
					description.append('NULL')
				#print (description[i])
				# creating dictionary for each item
				dict2[fields[i]]= description[i] 
				
				i = i + 1
				
		# creating json file		 
		out_file = open("Tshark.json", "a") 
		
		json.dump(dict2, out_file) 
		
		print("Finished json dump")
		out_file.close() 
		out_file2=open("Tshark.json",'a').writelines(["\n"])

		# appending the record of each employee to 
		# the main dictionary 
		#dict1[sno]= dict2 
		#l = l + 1




