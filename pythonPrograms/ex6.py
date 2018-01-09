# eg of while loop

n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff')
print(n)

# eg of Infinite loop

x = 3

while x > 2 :
    print('hi', x)
    break
print('otside the loop')




while True :
    line = input('>')
    
    if line[0] == '#' :
        continue            # it will point to the top of the loop i.e. while 
    
    if line == 'done' :
        print('inside if statement1', line)
        break                                   #it will point to out of the loop i.e while loop
        print('inside if statement2', line)
        
    print('outside if statement '+ line)            #why it's not printing this if i entered #gh then done
    break
print('outside while loop')