#num = int(input('enter the num'))
#x = range(num)
# for i in x :
#    if( num/i) == 0 :
 #       print(i)
        
        

score = float(input("Enter Score:"))
if score >= 0.9 :
    print('A')
elif score >= 0.8 :
    print('B')
elif score >= 0.7 :
    print('C')
elif score >= 0.6 :
    print('D')
elif score < 0.6 :
    print('F')
else :
    print("value is out of range")
        
        
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')