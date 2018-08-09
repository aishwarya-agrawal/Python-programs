num = [x for x in range(1,101)]
num[79]=0
print(num)
sum2 = 0
for i in range(1,101):
	sum2 = sum2+i
sum1 = 0
for i in range(0,100):
	sum1 = sum1+num[i]
if sum1 != sum2:
	n = sum1-sum2
print(abs(n))
