name = input('enter file')
handle = open(name)

for line in handle :
    words = line.split()
    print(words)
 