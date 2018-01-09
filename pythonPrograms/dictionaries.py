# Dictionaries

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)

ddd['age'] = 23
print(ddd)

# dictionary Literals (Constants)

jjj = {'chuck' : 1 , 'fred' : 42, 'jan' : 100}
print(jjj)

ooo = {}        # empty dictionary
print(ooo)

# Counting the words in a dictionary

name = dict()
name['csev'] = 1
name ['cwen'] = 1
print(name)

name['cwen'] = name['cwen'] + 1
print(name)


# Dictionary Traceback

ccc = dict()
# print(ccc['csev'])

print('csev' in ccc)        # O/P True or False


# To add new entry 

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts :
        counts[name] = 1
        print('if loop ',counts)
    else :
        counts[name] = counts[name] + 1
        print('else loop ',counts)
print(counts)


# get() For Dictionary :- NO TRACEBACK
