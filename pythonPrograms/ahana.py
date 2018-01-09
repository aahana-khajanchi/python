print("Hi", end='')
print("Ahana")


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

x = 'From marquard@uct.ac.za'
print(x[14:17])             # count starts from zero, it will print 14,15,16th pos, it will exclude 17th pos


x = 'From marquard@uct.ac.za'
print(x[0:18])            # it will print 14,15,16th pos, it will exclude 17th pos


x = 'python'
print(x[0])