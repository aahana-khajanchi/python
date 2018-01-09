#counts = dict()
#name = ['csev', 'cwen', 'csev', 'zqian', 'cwen','bob']

#if name in counts :
 #   x = counts[name]
#else :
#    x = counts.get(name, 0)
    
#print('using get() for dictionary ', counts)

# ------------------- run above it's giving error--


# counting with get() using for loop

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1 
    print(counts[name], name)
    
    
# Counting pattern in Dictionary

counts = dict()
print("enter a line of text")
line = input('')
words = line.split()
print('words',words)

print('counting')
for w in words :
    counts[w] = counts.get(w,0) + 1
    print('key ',w , 'counts',counts[w])
    


# Definite Loops and Dictionaries

counts = {'chuck' : 11, 'fred' : 42, 'jan' : 100}
for key in counts :
    print(key, counts[key],'\n')
    
# Retrieving lists of Keys and Values

print('Retrieving lists of Keys and Values')
jjj = {'chuck' : 1, 'fred' : 23, 'jan' : 13}
print('list is :- ',list(jjj))
print('the keys in the dictionary are :- ',jjj.keys())
print('the values in the dictionary are :- ',jjj.values())
print('the items consist of key n values :- ',jjj.items(),'\n')


# TWO Iteration Variable

print('TWO Iteration Variable')
jjj = {'chuck' : 1 , 'fred' : 42, 'jan' : 100}
for aaa,bbb in jjj.items() :
    print('keys are :-  ',aaa,'; values are :- ', bbb)
    

    