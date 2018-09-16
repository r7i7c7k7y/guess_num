import random
x = input('輸入猜數字的範圍,1~x,請輸入x :')
x = int(x)
r = random.randint(1, x)
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
	
