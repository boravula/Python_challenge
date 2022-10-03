#Import csv module
import os
import csv 
budget_data = os.path.join("Resources", "budget_data.csv")
#Open file and ignore headers
with open(budget_data) as csvfile: 	
	csvreader = csv.reader(csvfile, delimiter=',')

	header=next(csvreader)
	
	    #Prepare variables
		#Generate list for months and "profit & loss"
	months=[] 
	profitlosses=[] 
	average_change=[]
	

	#Set start conditions
	total=0
	a_change=0
	m_change=0
	m_count=0
	delta1=-1000
	delta2=100000000000
	delta_line1=0
	delta_line2=0
	loop1=0
	loop2=0
	
	
	    #Read in each row of data after the header and write data into assigned lists
	for row in csvreader:
		#Assign column as month & Profit and loss
		month=row[0] 
		profitloss=row[1] 
		#Add next line to list months & Prolosses
		months.append(month) 
		profitlosses.append(profitloss) 
		#Count the total of months in the "Date" column	
		m_count = len(months) 
		#print(m_count)
		#print(months)
	
	    #Begin data analysis
	
	#First loop is through list profit and losses (loop1 asloop index counter)
for loop1 in range (m_count):
				#Calculate total amount
	total=total+int(profitlosses[loop1]) 
			#print(total)
			
			#Second loop is through list profit and loss (loop2 as loop index counter)
for loop2 in range (m_count-1):
	a_change=(float(profitlosses[loop2+1])-float(profitlosses[loop2])) #Calculate sum of changes
	print(f'hoo : {a_change}')
	average_change.append(a_change)
	if a_change>delta1: #Determine greatest increase
		delta1=a_change
		delta_line1=loop2
	if a_change<delta2: #Determine greatest increase
		delta2=a_change
		delta_line2=loop2


print(delta1, months[delta_line1+1], delta2, months[delta_line2+1])


# 	#print(a_change/(m_count-1))
# m_change=(float(profitlosses[loop2+1])-float(profitlosses[loop2])) #Calculate monthly change



# 	#print(delta1)
# 	#print(months[delta_line1+1])
	

# if m_change<delta2: #Determin greatest decrease
# 	delta2=m_change
# 	delta_line2=loop2
# else:
# 	delta2=delta2
	

	# print(delta2)
	# print(months[delta_line2+1])
	

	#generate output lines
	

analysis=f'\
	Financial Analysis\n\
	----------------------------\n\
	Total Months: {m_count}\n\
	Total Amount: ${total}\n\
	Average_change: ${round(sum(average_change) / len(average_change),2)}\n\
	Greatest Increase in Profits: {months[delta_line1+1]} (${int(delta1)})\n\
	Greatest Decrease in Profits: {months[delta_line2+1]} (${int(delta2)})\n'
	
# onscreen print
print(analysis) 	

	#Write into text file named pybank.txt
	
file1=open("pybank.txt","w") #Open or if file does not exist then create file named pybank.txt
file1.writelines(analysis) #Write analysis into pybank.txt
file1.close() #Close pybank.txt write mode




