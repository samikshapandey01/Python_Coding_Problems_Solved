import re

from collections import deque

class HTMLVerifier:

    def __init__(self, filename):
        self.d = deque() #stack to push and pop open tags in html document
        self.closed_tag=[] #list for closed tags and will be used to print unbalanced closed tags at end
        self.filename = filename
        with open(filename,'r') as file:
            self.f=file.read()
    
    #Function to verify if html file is balanced or not 
    def verify_tag(self):
        ls=[] #intermediatory list for traversing through stack 
        tags=re.findall('<(/?[a-zA-Z0-9]+).*?>',self.f) #collect all the tag names in this list
        
        for tg in tags: 
            if ('/' not in tg): #if open tag then puch into stack d
                self.d.append(tg) 
                
            else:
                self.closed_tag.append(tg) #push closed tag to closed_tag list 
                
                for idx,open_tg in enumerate(reversed(self.d)): #traverse backwards through deque 
                    if (tg.replace('/','')==open_tg) and idx==0: # if closed tag equals last open tag in d  then pop item from stack and closed_tag and break the loop as this open tag is balanced.               
                        x=self.d.pop()                       
                        self.closed_tag.pop()
                        break
                    elif (tg.replace('/','')==open_tg) and idx!=0: #if its not last open tag then pop that tag from deque. 
                        while idx>=0:
                            if idx!=0:
                                ls.append(self.d.pop())
                            else:
                                y=self.d.pop()
 
                                self.d.extend(list(reversed(ls))) #append the unmatched open tags in between back to deque.
                                ls=[]
                            idx-=1
                        self.closed_tag.pop()
                        break
                    else:
                        continue
        if len(list(self.d)+self.closed_tag): #if at end items remain in deque and closed_tag list then html is not balanced.
            print("HTML document is not Balanced")
        else:
            print("Balanced")
                
    #Function to print unbalanced tag
    def print_unbalanced_tag(self):
            utg=list(self.d)+self.closed_tag
            u_list=['<'+i+'>' for i in utg]
            if len(utg):
                print("unbalanced tags:",u_list)
            else:
                print("HTML is balanced")
                
#ht=HTMLVerifier('samp.html') #provide html file name

#ht.verify_tag() #validate if file is balanced or not

#ht.print_unbalanced_tag() #print unbalanced tags