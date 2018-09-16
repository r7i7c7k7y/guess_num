import random
start = input('輸入猜數字的起始範圍:')
end = input('請輸入猜數字的結束範圍:')
start = int(start)
end = int(end)
r = random.randint(start, end)
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
	
