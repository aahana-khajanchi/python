import re 
x = 'My 2 fav no. Are 12 and 137'
y = re.findall('[0-9]+', x)     #
print(y)

y = re.findall('[AEIOU]+', x)       #  uppercase AEIOU      + means greater than 1
print(y)

z = 'From: Using the : character'
p = re.findall('^F.+:',z)          # Greedy prefers the longest
print(p)


# Non - Greedy prefers the shortest that's why we use ? 

import re
a = 'From: Using the : character'
b = re.findall('^F.+?:',a)
print(b)


# To extract particular portion 

a = 'From abcvs.gysgh@dwdg.ac.com sat jan 6 09:08:2017 2008'
print('using greedy')
c = re.findall('\S+@\S+',a)
print(c)
print('using non-greedy')
c = re.findall('\S+@\S+?',a)
print(c)


y = re.findall('\S+@\S+',a)
print(y)
y = re.findall('^From (\S+@\S+)',a)     # Parentheses are used to identify from where to start and stop n what string to extract
print(y)



# Extracting a host name - using find and string slicing

print('using find and string slicing')
atpos = a.find('@')
print(atpos)

sppos = a.find(' ',atpos)
print(sppos)

host = a[atpos+1 : sppos]       # from atpos to sppos it will print
print(host)


# Can do it using double split

print('using double split')
word = a.split()
print(word)
w = word[1].split('@')
print(w[1])


# Can do it using RegEx

import re
print('using RegEx')
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)', lin)
print(y)


y = re.findall('From .*@([^ ]*)', lin)
print(y)
