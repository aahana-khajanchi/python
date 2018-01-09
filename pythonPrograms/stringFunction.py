fruit = 'banana'
for i in fruit:
    print(i)
print('done')


index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1
print('done')


# to count the particular letter

word = 'ninni'
count = 0
for i in word:
    print(i)
    if i == 'a' :
        count = count + 1

print('total no. of times a in the word are', count)


# Slicing strings

word = 'aahana khajanchi'       # a is on 0 position
print(word[0:3])        # word[start,stop]  that's why it's like 0,1,2 position
print(word[5:8])        # 5,6,7 position

print(word[:])
print(word[0:])


# String Comparison

word = 'Ninni'                      # A < a  and Z < a like that we compare

print(ord('N'))

print(ord('b'))

if word == 'banana':
    print ('all right, bananas.')
    
if word < 'banana' :
    print('Your word,'+ word +' , comes before banana')
elif word > 'banana':
    print('your word,' + word +', comes after banana')
else :
    print('all right, banana. ')
    
    
# string library

greet = 'HeY'
zap = greet.lower()
print(zap)
print(greet)
print('HI , THERE'.lower())
print(greet)
print('HI , THERE'.upper())

# searching a string

fruit = 'mango'     # always index start from 0
pos = fruit.find('ng')
print(pos)

aa = fruit.find('aased')
print(aa)


# search and replace

greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)
nstr = greet.replace('o','X')
print(nstr)

# stripping or removing whitespaces

greet = '          Hello Bob       '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

# Prefixes

line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('please'))

# Parsing and Extraction
data = 'abcdef @ygyg gsg'
pos = data.find('@')
print(pos)

pos1 = data.find(' ',pos)
print(pos1)

pos2 = data[pos+1 : pos1]
print(pos2)