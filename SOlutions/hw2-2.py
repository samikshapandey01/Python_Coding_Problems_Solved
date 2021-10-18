score= input("Enter score:")
# using isdigit() + replace() 
# Check for float or number string 
isnum = score.replace('.', '', 1).isdigit()
if isnum and float(score) >=0 and float(score)<=1: #check if input string is number and liew within the range(0,1) inclusive
    score=float(score)
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")   
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
else:
    print("Bad score")