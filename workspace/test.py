x = 5
y = 15
a = list(range(x))
b = list(range(y-x,y))
c = a + b

d = range(20)
d1= list(d)
print (type(d),type(a))

print ('list a, ',a)
print ('list b, ',b)
print ('list c, ',c)
print ('  d, ',d)


print ('list d1, ',d1)

wait = input("按Enter結束程式")
