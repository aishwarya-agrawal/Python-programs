import random
l = [random.randint(89,100) for x in range(0,10)]
print(l)

for i in range(0,11):
	for j in range(i+1,10):
		if l[i]==l[j]:
			l[j]=0

print(l)

num = 90
for i in range(0,10):
	if l[i]==num:
		l[i]=0
for i in range(0,10):
	if l[i]==0:
		for j in range(i,10):
			l[i] = l[j]
print(l)