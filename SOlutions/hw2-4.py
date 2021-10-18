l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Input list is {l1}')

#a. [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
la = [i+5 for i in l1]
print(la)

#b. [1, 3, 5, 7, 9]
lb=[i for i in l1 if i%2==1]
print(lb)

#c. [1, 9, 81, 729, 6561]
lc=[9**i for i in l1 if i<5]
print(lc)

#d. [0, 3, 4, 9, 8, 15, 12, 21, 16, 27] 
ld=[i*2 if i%2==0 else i*3 for i in l1]
print(ld)

#e. [1, 3, 10, 14, 18]
le=[i*2 if i >=5 else i for i in l1 if i%2==1]
print(le)