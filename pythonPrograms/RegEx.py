# Searching line using find()

hand = open( 'abc1.txt')
counts = dict()

for line in hand :
    #line = line.rstrip()
    words = line.split()
    
    if line.find( 'subject') >= 0:
        print(line.find( 'subject'))
        print(line)
        
    for word in words :
        counts[word] = counts.get(word,0) + 1
        print('word:-', word,'counts[word]:-ss',counts[word])


          
# Searching line using RegularExpression  

import re                   # importing regular expression
hand = open('abc1.txt')
counts = dict()

for line in hand :
    line = line.rstrip()
    words = line.split()
    if re.search('subject', line) :
        print(line)
    
    for word in words :
        counts[word] = counts.get(word,0) +1
        print('word :- ',word,'counts[word] :- ',counts[word])
        