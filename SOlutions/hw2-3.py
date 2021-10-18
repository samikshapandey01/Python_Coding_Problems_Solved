# function with  list of email addresses (strings) as input and list of usernames as ouput
def extract_usernames_domains(emails): 
    user_name=[i.split('@')[0] for i in emails]
    return user_name

emails = ["apple@gmail.com", "orange@yahoo.com", "grape@abc.net"] 
usernames=extract_usernames_domains(emails) 

#print list strings returened by function with double qoutes
print("usernames == ",str(usernames).replace("'", '"'))