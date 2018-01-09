def thing() :                          #This is only a definition (def) part if u won't call then it won't execute
    print('inside the function 1')         #this is a stored and if we didn't call then it won't print anything
    print('inside the function 2')


print('outside function')
thing()                                    # call, invoke or reuse the function which we defined earlier in our code


# another eg

big = max('Hello world 1')      # max took the largest which was lowercase w
print(big)

tiny = min('Hello world2')
print(tiny)                     # tiny took the smallest letter which was space

def greet():
    return "Hey"
             
def greet(lang) :
        if lang == 'es' :
            print('Hola')
        elif lang == 'fr' :
            print('Bonjour')
        else :
            print('Hello')
            

greet('en')

greet('es')

greet('t')

greet('fr')



print(greet())