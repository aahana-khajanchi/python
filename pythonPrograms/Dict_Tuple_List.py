fhand = open('abc1.txt')
counts = dict()
print('counts', counts)

for line in fhand :
    words = line.split()
    print('words', words)
    
    for word in words :
        counts[word] = counts.get(word, 0) + 1
        print('word --> ',word,'counts[word]-->', counts[word])
        
print('words :- ', words)
print('counts :- ', counts)
        
        
        
lst = list()
for key, val in counts.items() :
    newTup = (val, key)
    lst.append(newTup)
    
print('list :- ',lst)


lst = sorted(lst, reverse = False)
print('list in order',lst)


lst = sorted(lst, reverse = True)
print('list in reverse order',lst)



for val, key in lst[:10] :
    print(key, val)


# -------- Either u can do this or use the FOR-All Loop    
 
#  lst = list()
#  for key, val in counts.items() :
#  newTup = (val, key)
#  lst.append(newTup) 
    
print('using for all loop')    
print( sorted ( [ (v,k) for k,v in counts.items() ] ) )         # this is called FOR-ALL Loop

    