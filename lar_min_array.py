import random
ar = [random.randint(1,100) for x in range(1,50)]
print(ar)
max = ar[0]
min = ar[0]
for k in range(0,len(ar)):
	if(ar[k]>max):
		max = ar[k]
	if min > ar[k]:
		min = ar[k]
print(max)
print(min)

