# Strings and Lists

abc = 'With three words'
stuff = abc.split()

#Strings
print(stuff)
print(len(stuff))
print(stuff[0])

# Lists
print(stuff)
for w in abc :
    print(w)
for w in stuff :
    print(w)

    
# using split() in a string   # if we use split then we don't hv to search for spaces n all

line = 'A lot              of spaces'
etc = line.split() 
print(etc)

line = 'first;second;third'
thing = line.split()        # as we didn't specify the split & there is no white spaces therefore it will consider it as a full string
print(thing)            

print(len(thing))


thing = line.split(';')     # we specified split that's why first second n third will be 3 different words
print(thing)
print(len(thing))

# to get the data using split rather than searching for any white space

fhand = open('abc2.txt')
for line in fhand :
        line = line.rstrip()
        if not line.startswith('From') : continue
        words = line.split()
        print(words[2])
        print(line)
        print(words)
words = line.split()

        
