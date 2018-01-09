# To open the file

fhand = open('abc.txt','r')
print(fhand)


# Counting Lines in a file

fhand = open('abc.txt')
count = 0
for line in fhand :
    count = count + 1
print('line count is ',count)


# Reading the *whole* file

fhand = open('abc.txt')                         #From stephen.marquad@uct.ac.za Sat Jan 5 09:14:16 2008
inp = fhand.read()                                                #Return-Path: <postmaster@collab.sakaiproject.org>
print(len(inp))                                               #Date: Sat, 5 Jan 2008 09:12:18 -0500
print('reading line upto 20 charcater :-',inp[:20])


# Searching Through a File

fhand = open('abc.txt')
for line in fhand :
    if line.startswith('From') :
        print('searched line which starts with From is :-',line)
        
# removing the white spaces
        
fhand = open('abc.txt')
for line in fhand :
    line = line.rstrip()            # rstrip() will remove the white spaces
    if line.startswith('From') :
        print('searched line which starts with From is :-',line)
        
# Skipping with Continue

fhand = open('abc.txt')
for line in fhand :
    line = line.rstrip()            # rstrip() will remove the white spaces
    if not line.startswith('Date:') :
        continue                        # it will select particular lines which starts with Date
    print("searched line which starts with Date is :-",line)
      

# using in to select lines

fhand = open('abc.txt')
for line in fhand :
        line = line.rstrip()
        if not '.com' in line :
            continue                  # it will select particular lines which has .com 
        print('particular lines hving .com :- ', line)    
        
# search from a particular file    # doubt - not working    
        
fname = input('Enter the file name:   ')
fhand = open(fname)
count = 0
for line in fhand :
            if line.startswith('subject') :
                count = count + 1
print('There were',count,'subject lines in ', fname)
        
        
# bad files name we use Try - Except

fname = input('enter file name: ')

try :
    fhand = open(fname)
except :
    print('file cannot be opened: ', fname)
    quit()      # it won't execute the further files

count = 0
for line in fhand :
    if line.startswith('subject') :
        count = count + 1
print('There were ', count, 'subject lines', fname)