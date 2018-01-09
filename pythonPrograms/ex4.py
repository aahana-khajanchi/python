
eee = 'hello' + 'there'
#eee = eee + 1              
# print (type(eee))       # It will give an error:  can't convert 'int' object to str 
bob = 'abc'
bob1 = 'def'
total = bob + bob1
print('total is',total)
print ( eee )


eee1 = 123
eee1 = eee1 + 1
print (type(eee1), eee1)

print (type('hello'))

print (type(1))

print ( float(99) + 100)




sav1 = '123'
print (type(sav1))
#print (sav1 + 1)     # TypeError: must be str, not int


sav1 = int ( sav1)
type( sav1)
print ( sav1 + 1)

#print (int (eee))     #ValueError: invalid literal for int() with base 10: 'hellothere'  [base 10 means integer, similar to base 16 is hexadecimal]
