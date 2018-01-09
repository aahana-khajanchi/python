astr = 'hello Bob'
try :
    print('hello')
    istr = int(astr)
    print('hello')
except :  
    print('except block')                           # we use this try-except to handle Traceback
    istr = -1
    
print('First', istr)

astr = '123'
try :
    istr = int(astr)
except:
    istr = -1
    
print('second', istr)



print('another example')

rawstr = input('Enter a number\n')
try :
    iva1 = int(rawstr)
except :
    iva1 = -1
    
if iva1 > 0:
    print('nice work')
else :
    print('not a number')


