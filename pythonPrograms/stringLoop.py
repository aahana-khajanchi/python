
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
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1
print('done')
