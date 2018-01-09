             
def greet(lang) :
        if lang == 'es' :
            return 'Hola'
        elif lang == 'fr' :
            return 'Bonjour'
        else :
            return 'Hello'
            

print(greet('en')+'Aahana')

print(greet('es')+'Ninni')

print(greet('t'),'shreya')

print(greet('fr'),'shruti')

fruit = 'mango'
if 'a' in fruit :
    print('found it')


def add(a,b) :
    return (a+b)
 
x = add(1,2)
print('sum is ', x)




print('aahanaagaa'.rfind('a'))
print('ababbb'.rfind('b',0))


fruit = 'abc'
print(len(fruit))
