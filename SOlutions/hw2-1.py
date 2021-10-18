while True:
    dec=input("Enter a Number : ")
    if dec.lower() =='end':
        break
    else:
# using isdigit() + replace() 
# Check for float or number string 
        dig = dec.replace('.', '', 1) #replace first occurence of . in input string
        dig_neg= dig.replace('-','',1) # extra step for negative numbers
        res = dig_neg.isdigit()  
        if res: 
            dec_indx=dec.find('.') #find index for .
            dec_cnt=dec.count('.') #count number of . in input string
            if dec_indx>=0:
                de_part=dec[dec_indx:]
                dec_part_f=float(de_part)
                print(dec_part_f)
            else:
                print('0')
        else:
            print("Enter a valid number")