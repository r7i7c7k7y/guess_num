import random
r = random.randint(1, 100)
n = 0
while True:
	n = n + 1
	ans = input('猜數字吧 :')
	ans = int(ans)
	if r == ans:
		print('猜對拉 !')
		break
	else:
		if ans > r:
			print('太大了拉')
		else:
			print('太小了拉')
print('總共猜了',n,'次')
	
