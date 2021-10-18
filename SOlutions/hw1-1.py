# Using python built in string methods to calculate length and counts

giv_str="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
len_str=len(giv_str) #using len string method to calculate length of string 
cnt_a=giv_str.count('A') #using count method to calculate count of 'A' in given string
cnt_t=giv_str.count('T')
perctg_a_t=(cnt_a+cnt_t)/len_str #total count of A and T divided by total length gives the percentage of A and T
print(f"Given string: {giv_str}")
print(f"length: {len_str}")
print(f"A count: {cnt_a}")
print(f"T count: {cnt_t}")
print(f"Percentage of A & T: {perctg_a_t}")