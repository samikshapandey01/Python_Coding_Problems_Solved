#Generator function which each reads each file in the director and perform following functions:
#    1.Reads file and skips first header line
#    2.Split the comma separated file using strip
#    3.Yield flight number from 5th column
def gener(file):
    with open(file, 'r') as f:
        first_line=f.readline() #This will read first line and will skip it when we read from file below
        for line in f:
            flight_no=line.strip().split(',')[4]
            yield flight_no
            
                    
import os
import glob

dt={} #dictionary for storing flight# and total no of flights by airline and then sorting by no of flights 


#Read all csv files from data sub directory and call generator and add flight# into dictionary
#Data subdirectory is in the directory where we ran this python program.Using glob to list all csv files in data subdirectory
for file in glob.glob("data/*.csv"):
    m=gener(file) 
    for fl in m:
        dt[fl]=dt.get(fl,0)+1

#Sort dictionary on descending order
st=sorted(dt.items(),key=lambda x:x[1],reverse=True)

output_file=open('flights_by_airline.csv','w')

tot_flights=0
output_file.write("Airline,# Flights\n") #Writing header to output file

#Loop through dictionary and write into output files
for fl,no in st:
    output_file.write(f"{fl},{no}\n")
    tot_flights=int(no)+tot_flights

output_file.write(f"Total ,{tot_flights}")

output_file.close()
