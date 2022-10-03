#Import csv module
import csv 
	
#Start csv file handling
with open ('Resources\election_data.csv') as csvfile:
    #Specify delimiter and variable that holds contents and read header
	csvreader=csv.reader(csvfile, delimiter=',') 
	header=next(csvreader) 
	

	#Prepare variables
	#Generate list named "voterids" - "Voter ID", "counties" - "County", "candidates" - "Candidate", total votes, result printout, percentage of votes  for each candidate in columns
	voterids=[] 
	counties=[] 
	candidates=[] 
	candidatenames=[] 
	totalpereachcand=[] 
	resultprintcan=[] 
	totaleachcanperc=[] 
	winner=""
	

	#Set start conditions
	line_count=0
	winnervotes=0
	loservotes=0
	
	    
	#Read in each row of data after the header and write data into assigned lists
	for row in csvreader:
            voterid=row[0] #Assign column 0 as voterid
            county=row[1] #Assign column 1 as county
            candidate=row[2] #Assign column 2 as candidate
            voterids.append(voterid) #Add next line to list voterids
            counties.append(county) #Add next line to list counties
            candidates.append(candidate) #Add next line to list candidates
	    
            line_count= len(voterids) #Count the total number of votes cast in the "Voter ID" column
	    
	    #print(line_count)
	

	#Begin data analysis
		
candidatenames.append(candidates[0]) #Pre-loadfirst candidate name for comparison
	

	#First loop is through the list of candidates to determine candidates voted for (variable loop1 as loop index counter)
for loop1 in range (line_count-1):
	    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in candidatenames:
	        candidatenames.append(candidates[loop1+1])
	

n=len(candidatenames)
	
	#print(n)
	
	#Second loop variable loop2 as loop index counter
for loop2 in range (n): #Range of loop depending on how many candidates were found
	totalpereachcand.append(candidates.count(candidatenames[loop2])) #Count total votes of candidates and add to list total
	totaleachcanperc.append(f'{round((totalpereachcand[loop2]/line_count*100), 4)}%') #Calculate % per candidate found
	if totalpereachcand[loop2]>winnervotes: #Find candidate with highest vote count
		winner=candidatenames[loop2]
		winnervotes=totalpereachcand[loop2]
				

	#3rd loop variable loop4 as loop index counter
for loop4 in range(n):
	resultprintcan.append(f'{candidatenames[loop4]}: {totaleachcanperc[loop4]} ({totalpereachcand[loop4]})') #Format list resultprintcan

#Prepare new combined list of results for printout each candidate
resultlines='\n'.join(resultprintcan) 

	
	#Generate output lines
	
analysis=f'\
	Election Results\n\
	----------------------------\n\
	Total Votes: {line_count}\n\
	----------------------------\n\
	{resultlines}\n\
	----------------------------\n\
	Won: {winner} Winner\n\
	----------------------------\n'
	

print(analysis) #Output results on screen
	
	#Write into text file named pypoll.txt
	
file1=open("pypoll.txt","w") #Open or if file does not exist then create file named pypoll.txt
file1.writelines(analysis) #Write analysis into pypoll.txt
file1.close() #Close pypoll.txt write mode

    
