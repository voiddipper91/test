x = 5
y = 15
a = list(range(x))
b = list(range(y-x,y))
c = a + b

d = range(20)
print (type(d),type(a))

print ('list a, ',a)
print ('list b, ',b)
print ('list c, ',c)

wait = input("按Enter結束程式")
