# Searching line using Startswith()

hand = open('abc1.txt')
for line in hand :
    #line = line.rstrip()
    if line.startswith('aa') :
        print('line is :- ',line)
        
        
# Searching line using RegularExpression        
        
import re

hand = open('abc1.txt')
for line in hand :
            #line = line.rstrip()
            if re.search('^subject',line) :     # ^ = start of the beginning
                print(line)
                

                
                
# Using more RegExp

print('^X-\S+:')

hand = open('abc1.txt')
for line in hand :
            #line = line.rstrip()
            if re.search('^X-\S+:',line) :     # ^ = start of the beginning
                print(line)