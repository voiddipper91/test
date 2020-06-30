# _*_ conding: utf-8 _*_


import random

game_count = 0
all_count = []

while True:
	game_count += 1
	guess_count = 0
	answer = random.randint(0,99)
	while True:
		guess = int(input("請猜一個數字(0-99):"))
		guess_count += 1
		if guess == answer:
			print("恭喜你猜中了")
			print("你總共猜了" + str(guess_count) + "次")
			all_count.append(guess_count)
			break;
		elif guess > answer:
			print("你猜得太大了")
		else:
			print("你猜得太小了")
	onemore = input("還要再玩一次嗎(Y/N)?")
	if onemore != 'Y' and onemore != 'y':
		print('你的成績如下:')
		print(all_count)
		print("平均猜中次數" + \
			 str(sum(all_count)/float(len(all_count))))
		break;
			
wait = input("按任意按鍵離開")
