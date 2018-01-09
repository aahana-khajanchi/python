#Tuples and dictionaries

d = dict()
d[ 'abc' ] = 2
d[ 'def' ] = 4
for (k,v) in d.items() :
    print(k, v)
    
tups = d.items()
print(tups)


#Comparing tuples

print( (0, 1, 2) < (5, 1, 2))                       # 0 < 5 that's why it won't compare 1,2 to another 1,2
print( (0,1,20000000) < (0, 3, 4))                      # 0 is same, so it will compare 1 n 3 in which 1< 3 so it won't compare 20000 < 4
print( ( 'Jones', 'Sally' ) < ( 'Jones', 'Sam'))        # l<m as others r same
print( ( 'Jones', 'Sally' ) > ( 'Adams', 'Sam'))          # only comparw Jones n Adams n won't compare the next 2


# Sorting list of tuples only using KEYS

d = { 'a' : 10, 'c' : 1, 'b' : 22}
print(d.items())
print(sorted(d.items()))

# ---------

d = { 'a' : 10, 'c' : 1, 'c' : 22}
print(d.items())
print(sorted(d.items()))

d = { 10 : 10, 20 : 1, 15 : 20}     # keys can't be same, values can be same
print(d.items())
print(sorted(d.items()))


# using sorted() in for loop

d = {'a' : 10, 'b': 1, 'c' : 22}
t = sorted(d.items())
print(t)

print("using for loop")
for key,value in sorted(d.items()) :
    print(key,value)
    
# sort by values instead of a key n We can construct a list of tuples of the form (value, key)

print('print having values 1st n then keys')
c = {'a': 10, 'b' : 1, 'c' : 22}
tmp = list()
for k,v in c.items() :
    tmp.append( (v,k) )  
print(tmp)


print('sort using values from high to low i.e. descending order')
tmp = sorted( tmp, reverse = True)      # for descending order we use reverse = True
print(tmp)

print('sort using values from low to high i.e. ascending order')
tmp = sorted( tmp)      
print(tmp)


