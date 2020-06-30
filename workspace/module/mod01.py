def test11(a,b,c,d):
	c = a+b
	d = a-b
	return c,d

def levelss(sorce):
	y={}
	#sorce =int(input("請輸入分數(0-100):"))
	level = int(sorce) // 10
	if level == 10:
		y['level']='滿分'
	elif level == 9:
		y['level']='A'
	elif level == 8:
		y['level']='B'
	else:
		y['level']='請繼續努力'
	return y


#print(levelss(49))

# abc={}
# abc['aaa']='bbb'
# print(abc)

