#a= list(range(12))
#b= list(range(22))
#for b in a:
#	print (a,'\n',b)
	# c = a + b
	# print(c)
	# c.sort()
	# print(c)
	# c.reverse()
	# print(c)
	# d ={}
	# d['x'] = 9
	# d['y'] = 8
	# d['z'] = 5
	# print(d)
	# e = d.items()
	# print (e)
	# msg = 'the world'
	# f = [1,2,3,4,5,6,7]
	# g = len(f)
	# i = {'aa':5,'bb':'bsac'}
	# j = len(i)
	# print(len(msg),g,j)


def test6(n,sym="*"):
	for i in range(1,n+1):

		print(sym,end='' )		

#print (test6(7,'#'))


# def test7(a,b,x):
# 	#global d
# 	global tt 
# 	c = a+b
# 	d = a+b
# 	tt = a+b
# 	print('在函數中，C={}、D={}'.format(c,d))
# 	return tt
	
	
# tt=0
# c=6
# d=988

# print('在呼叫def前，C={}，D={},tt={}'.format(c,d,tt))
# print('{}+{}={}'.format(2,2,test7(2,2,2)))
# print('在呼叫def後，C={}，D={},tt={}'.format(c,d,tt))



#sss = lambda a,b:a+=b
#print(sss(2,2))

# def outer():
# x = 10
# def inner():
# 	print(x)
# inner()
# x = 20
# return inner

# # f = outer()
# # f()


#wait = input()

from module import mod01

# xx = mod01.test11(1,2,3,4)
# print (xx)
# print(type(xx))



x = mod01.levelss(49)
print(x['level'])

wait =input()