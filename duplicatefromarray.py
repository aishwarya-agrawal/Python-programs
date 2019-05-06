import random
l = [random.randint(89,100) for x in range(0,10)]
print(l)
for i in range(0,10):
	numb = l[i]
	for k in range(0,10):
		if l[k] == numb:
			if k!=i and l[i]!=0:
				l[k] = 0

print(l)