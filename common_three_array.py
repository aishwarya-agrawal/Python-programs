import random
l1 = [random.randint(1,10) for x in range(0,5)]
l2 = [random.randint(1,10) for x in range(0,5)]
l3 = [random.randint(1,10) for x in range(0,5)]
result = []
print(l1)
print(l2)
print(l3)
#method1
for i in range(0,len(l1)):
	for j in range(0,len(l2)):
		if l1[i]==l2[j]:
			for k in range(0,len(l3)):
				if l1[i]==l3[k]:
					result.append(l1[i])
print(result)
