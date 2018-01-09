# list of integers
print([1,24,76])

# this eg has diff type of data i.e strings, int, float, list inside list
print(['red', 24, 98.6, [5,6],90,'blue',[],'black'])

list = [12,10,14,20,'dg',23.09,4]
for i in  list:
    print(i)
    
print('the 2nd pos in the list is ',list[2])        # looking inside list
    
# Strings are IMMUTABLE (Don't change)    

fruit = 'Banana'
# fruit[0] = 'b'     # gives traceback error as string are immutable

x = fruit.lower()
print(x)


# Lists are MUTABLE (Changeable)

lotto = [2,19,23,10,4]
print(lotto)
lotto[2] = 28
print(lotto)
    
#Length of a list

greet = 'aahana jain'
print('length of the string -aahana jain  is ',len(greet))

x = [1, 2, 'ninni', 9.9]
print('length of diff data type is',len(x))


# Using the range function

print(range(4))

friends = ['john', 'Jane', 'Mary']
print('length of the string is ',len(friends))

print('range of the above string',range(len(friends)))          # range always start from 0

# Printing the list with and without using range() - both the output will be same

friends = ['john', 'Jane', 'Mary']

for friend in friends :
    print('Happy new Year:- ', friend)
 

 
for i in range(len(friends)) :          # Counted loop
    friend = friends [i]
    print('Happy new year: ', friend)


