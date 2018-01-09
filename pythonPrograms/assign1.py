hrs = input('enter hrs')
rate = input('enter rate ')  

# pay = hrs * rate; anything in input is taken as a string so convert into either int or float
pay = int(hrs) * int(rate)                # here if u give float it will give an error
print(pay)                       # TypeError: can't multiply sequence by non-int of type 'str'

hrs = input('enter hrs')
rate = input('enter rate ')
pay = float(hrs) * float(rate)
print(pay) 

hrs = float(input('enter hrs'))
rate = float(input('enter rate '))
pay = hrs * rate
print(pay) 


x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
  print('All done')         # indentation error