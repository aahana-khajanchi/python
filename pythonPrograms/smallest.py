smallest = None
for value in [12,13,2] :

    if smallest == None :                              # or u can use -> if smallest is None    ['is' it's an operator]
        smallest = value
        print('hey')

    elif smallest > value :
        smallest = value
        print('hi')
        
    print(smallest, value)
print('smallest number is ', smallest)


list = [12,3,123,24]

small = None
for val in list :
    if small == None :
        small = val
        
    elif small > val :
        small = val
print('smallest value is ',small)