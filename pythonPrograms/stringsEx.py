#name = input('Enter:')
#print(name)
#apple = input('Enter:')
#x = apple - 10          # it will give type error

#x = int(apple) - 10
#print(x)



fruit = 'abcdef'
letter = fruit[1]
print(fruit)
print(letter)

x = 5
w = fruit[ x - 2]
print(w)

print(len(fruit))


# Looping through Strings

print('ex of  Looping through Strings')

fruit = 'banana'
x = len(fruit)

for i in range(0,x) :
    letter = fruit[i]
    print(i,letter)
print('done')

# or we can use while loop

index = 0
while index < x :
    letter = fruit[index]
    print(index, letter)
    index = index + 1           # if u forget this then it will go into infinite loop
print('done')
