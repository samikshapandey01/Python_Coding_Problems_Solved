import re
from collections import Counter

user_inp=input("Enter length of word and # terms to return:")
word_len,no_words=re.findall('\d+',user_inp)

with open('sonnet.txt') as f:
    file_tot=f.read()
    pattern='\\b[a-zA-Z]{'+word_len+'}\\b'  #Pattern to extract words with word length as input by user
    words=(re.findall(pattern,file_tot.lower()))
    word_cnt=Counter(words)

    print(f"\nTop {no_words}, length of word: {word_len}")
    for word,count in word_cnt.most_common(int(no_words)):
        print(word, count)