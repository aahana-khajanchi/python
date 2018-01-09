# Concatenating Lists using +

a = [1,2,3]
b = [4,5,6]
print ('conacatenation of a list of numbers')
c = a + b
print(c)
print(a)

# Slicing of Lists

t = [9,41,12,3,74,15]       # indexing starts from 0
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

# Building a list from Scratch

stuff = list()
stuff.append('book')            #stuff = stuff.append(99)  DON'T PASS LIKE THIS -> O/P None
stuff.append(99)             # when u'll pass this stuff = stuff.append(99) then the O/P will be None
print(stuff)

stuff.append('ninni')
print(stuff)


# To check whether a particular no. is in a list or not 

some = [1, 3, 56, 23, 19]
print(1 in some)                # o/p will be either True or False
print(11 in some)
print(20 not in some)


# Lists are in Order

friends = ['Ninni','Aahana', 'Niriha']
friends.sort()
print(friends)
print(friends[0])


# Built-in Functions and Lists

nums = [3, 41, 121, -9, 74, 15]
print('total length is',len(nums))
print('max no. is',max(nums))
print('min no. is',min(nums))
print('Total sum of the no. is ',sum(nums))
print('average is ',sum(nums)/len(nums))


# to calculate avg using while loop

total = 0
count = 0
while True :
    inp = input('Enter a no. ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
    
average = total / count
print('Average:', average)

# To calculate avg using a list i.e. Data Structures

numlist = list()                # empty list which will contain all the elements
while True:
    inp = input('Enter a number:')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)           # it is having memory space

average = sum(numlist) / len(numlist)
print('Average: ', average)

