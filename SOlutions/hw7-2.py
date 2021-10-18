import re
from datetime import *


def file_cal(output): 

    file_dict={}
    pattern=re.compile('^[^d].{9}?\s+?\d+\s+?.*? (\d+) ([A-Z][a-z]{2}\s+?\d{1,2}\s+?[0-9]+?[:]?[0-9]+)\s+(.*)\n?',re.MULTILINE)
    file_data=re.findall(pattern,output)
    
    file_size=[int(i[0]) for i in file_data]
    print(f'Total File size: {sum(file_size)}')
    
    for dt in file_data:
        if re.search(':',dt[1]):
            dat=datetime.strptime(dt[1], "%b %d %H:%M")
            dat=dat.replace(year=2020)#Changing default year 1990 to current year 
        else:
            dat=datetime.strptime(dt[1], "%b %d %Y")
        file_dict[dt[2]]=dat
    
    latest_file = max(file_dict.items(), key=(lambda x: x[1]))
    earliest_file = min(file_dict.items(), key=(lambda x: x[1]))
    
    
    print('Latest Modified File : ',latest_file[0],latest_file[1].strftime('%b %d %Y %H:%M'))
    print('Earliest Modified File: ',earliest_file[0],earliest_file[1].strftime('%b %d %Y %H:%M'))
	

ls_output='''-rwxrwxrwx 1 user user 163483 Sep 8 03:29 DATA200 HW1.pdf
-rwxrwxrwx 1 user user 78995 Sep 15 23:03 DATA200 HW2.pdf
-rwxrwxrwx 1 user user 114964 Sep 29 02:10 DATA200 HW3.pdf
-rwxrwxrwx 1 user user 108137 Oct 7 23:00 DATA200 HW4.pdf
-rwxrwxrwx 1 user user 82301 Oct 13 17:13 DATA200 HW5.pdf
drwxrwxrwx 1 user user 82301 Oct 13 17:13 DATA200 HW6.pdf
-rwxrwxrwx 1 user user 82301 Oct 7 2009 DATA200 HW7.pdf
'''

file_cal(ls_output)