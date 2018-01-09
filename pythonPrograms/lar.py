largest = -1
list = [1,9,23,22,18]
for num in list :
    if num > largest :
        largest = num
print('largets no. is ',largest)

for num in list :
    if num > 18 :
        print ('students age greater than 18 is',num)
    
found = False
for num in list :
    if num == 18 :
        print(num)
    
flag = 0
sum = 0
for i in list :
    sum = sum + i
    flag = flag + 1
print ("sum is :  ",sum,"\n count is ",flag)


for i in list:
    avg = sum / flag
print('avg is ',avg)

smallest = 0
for num in list :
    flag = num
    smallest = flag
    if smallest < num :
        smallest = num
print("smallest no. is :", smallest)

small = None
for value in [12,13,2] :
    if small == None :
        small = value
        
    elif small > value :
        small = value
print('smallest value is ',small,'\nlist no. are ',value)


small = None
for value in [12,13,2] :
    if small == None :         # it won't work bcz u hv compared it to value rather than None 
        small = value
        
    elif small > value :
        small = value
print('smallest value is ',small,'\nlist no. are ',value)



astr = 'hello Bob'
try :
    istr = int(astr)
except :                               # we use this try-except to handle Traceback or any errors
    istr = -1
    
print('First', istr)

astr = '123'
try :
    istr = int(astr)
except:
    istr = -1
    
print('second', istr)



abc = dict()
print('labels or key and values can be strings or integers in dictionary :-  here key is 123 n value is abc')
abc = {123 : 'abc', 1233 :2}
print(abc[123])
print ('dictionary',abc)            # if u use print ('dictionary'+abc) it will gove an error as it shd be string
abcd = dict()
abcd = {1 : 2, 3 : 4}
print(abcd)
print(abcd[3])
abcd[3] = abcd[3] + 1
print(abcd) 
