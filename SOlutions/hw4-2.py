#function for pattern # d.
def func(num):
    if num%2==0:
        return num*2
    else:
        return num*3

l1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Pattern a. [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
m1=map(lambda x:x+5,l1)
print(list(m1))

#Patern b. [1, 3, 5, 7, 9]
m2=filter(lambda x: x%2==1,l1)
print(list(m2))

#Pattern c. [1, 9, 81, 729, 6561]
m3=map(lambda x:9**x,list(filter(lambda x:x<5,l1)))
print(list(m3))

#Pattern d. [0, 3, 4, 9, 8, 15, 12, 21, 16, 27]
#map function calls a function above which returns num*2 for even numbers and num*3 for odd numbers
m4=map(func,l1)
print(list(m4))

#Pattern e. [1, 3, 10, 14, 18]
#first filter odd numbers and than multiply by 2 if number is greater than 3
m5=map(lambda x:x*2 if x >3 else x,list(filter(lambda x:x%2==1,l1)))
print(list(m5))