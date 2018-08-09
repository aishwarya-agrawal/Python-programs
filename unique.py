import random
li = [random.randint(0,55) for x in range(0,50)]
li2 = []
li2.append(li[0])
f=0
k = []
for i in range(1,len(li)):
	for j in range(0,len(li2)):
		if li[i] == li2[j]:
			f = 0
			break
		else:
			f = 1
	if f == 1:
		k.append(li[i])
		f=0
print(k)