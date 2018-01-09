num = int(input('enter the number '))
for i in range(num):
    print('i is',i)
    x = i+1
    print('x is',x)
    if ((num % x) == 0) :
        print('num is',x)
        
        if (x % 2) == 0 :
            print(x)
        elif (x % 3) == 0 :
            print(x)
        elif (x % 5) == 0 :
            print(x)
        elif (x % 7) == 0 :
            print(x)
        elif (x % 11) == 0 :
            print(x)
        else :
            print('prime no.', x)