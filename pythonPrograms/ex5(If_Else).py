x = 1
for x in range(1,5) :
    print(x,'\n')
    if x > 2 :
        print('Bigger than 2',x)
    else:
        print('smaller then 2',x)
    print('done with x', x)


    a = 10                                     # only 1 statement will run either if or elif or else
    if a < 2 :                                 # this is called multi way looping
        print('a is small')    
    elif a < 10 :
        print('a is medium')
    elif a < 20 :
        print('a is medium')
    elif a < 30 :
        print('a is medium')
    else :                                      # it's not necessary to have else u can remove them
        print('a is large')

    print('hey')