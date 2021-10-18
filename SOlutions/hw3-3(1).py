#function 1 for generating keys for sorting word dictionary on wordcount first and word second
def sort_key(item):
    return item[1], item[0]

#Function2 for generating keys for sorting dictionary on length of word
def sort_key2(item):
    return len(item[0])

#read the file and separate words using space,store it in list and create a dictionary with word as key and wordcount as values
file_word=open('sonnet.txt','r')
word_dict={}
replace_txt=set('?!.,;:') #set of special characters to remove
word_list=file_word.read().split(' ') #creating a list of all words by splitting using space from file
file_word.close()
for word in word_list: 
    word=word.replace('\n','').lower() #remove new line characters and change all words to lower case
    for spc in replace_txt:
         word=word.replace(spc,'')
    if len(word)in range(2,11):  #select only words with length between 2 and 10
        word_dict[word] = word_dict.get(word,0)+1 #add word and wordcount to dictionary

#sort the dictionary first using count and word in reverse order and than sort on word length in ascending order
word_dict_sorted=sorted(sorted(word_dict.items(),key=sort_key,reverse=True), key = sort_key2) 
      
pointer,counter  = [0,0] #pointer to point to word_length list below and counter to print only 15 words of each length

word_length = [i for i in range(2,11)] #list to hold length of the words desired i.e 2 to 10 inclusive

#loop on sorted word list to print top 15 words of word lenght 2 to 10 starting with length 2
for val in word_dict_sorted:        
    if pointer >= len(word_length):  
        break #exit loop when pointer exceeds the maximun word lenght i.e 10
    if counter == 0 and len(val[0]) == word_length[pointer]:
        #print below line before printing first word of each word length
        print(f"Top 15, length of word: {word_length[pointer]}")
    #If to print the word and its count if len of the word is equal to word length list value    
    if len(val[0])  == word_length[pointer]:
        print (val[0],val[1])
        counter +=1
    if counter == 15   :
        pointer+=1 #pointer to point to next word length after we print 15 words of each word length
        counter =0 #reset the counter to ensure we print only 15 words of each length
        print()
