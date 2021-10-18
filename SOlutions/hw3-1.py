inp_list= [] # initialize list to store user input values 
while True:
    
    record=input("Enter grade record (press Enter to stop):")
    if len(record.strip())==0:
         break #break when no input is provided
    inp_list.append(record)
    
# Input Filename
file_name=input("Enter filename to save: ")

f = open(file_name, 'w')
f.write("\n".join(inp_list))

f.close()