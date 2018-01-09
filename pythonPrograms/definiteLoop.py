# ex of for loop

family = ['Mummy', 'Daddy', 'kuda']
for family1 in family :
    print('happy new year\t'+family1)
print('done!')


# to find the largest number

largest_num = -1
for the_current_num in [5,14,3,27,1000] :
    if the_current_num > largest_num :
        largest_num = the_current_num 
        print('largest so far is ', largest_num, 'the num is ', the_current_num)
    
print('largest no. is', largest_num)   



# to count total number in for loop or counting in a loop

zork = 0
for thing in [2,3,5,1,2,2,2,3] :
    zork = zork + 1
    print(zork, thing)
print('total count is',zork,'\n\n')


# To calculate sum of all the numbers in a loop  OR Summing in a loop

zork = 0
temp = 0
for thing in [9,41,12,3,74,15] :
    zork = zork + 1
    temp = temp + thing
    print('temp var is',temp,'original num is',thing)
    
print('total count is ',zork)
print('total sum is', temp)



# Average in a loop

count = 0
sum = 0
for value in [9,41,12,3,74,15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
average = sum/count
print('count is',count,'total sum is ', sum,'average is ',average,'\n\n')



# Filtering in a loop

for value  in [9,41,12,3,74,15] :
    if value > 18 :
        print('age is greater than 18,', value)
print('age is less than 18')


# to find a particular value

found = False
for value in [9,41,12,3,74,15] :
    if value == 74 :
        found = True
        print('yes 74 is present in the list',found)
    print(found, value)
print('out of the for loop \n', found,'\n')


# To find smallest value in the loop

smallest = None
for value in [9,41,12,3,74,15] :

    if smallest == None :                              # or u can use -> if smallest is None    ['is' it's an operator]
        smallest = value
        print('hey')

    elif smallest > value :
        smallest = value
        print('hi')
        
    print(smallest, value)
print('smallest number is ', smallest)
