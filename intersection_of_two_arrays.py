import random
ar1 = [random.randint(1,50) for x in range(1,5)]
ar2 = [random.randint(1,50) for x in range(1,5)]
print(ar1)
print(ar2)
ar3 = []
for i in range(0,len(ar1)):
	for j in range(0,len(ar2)):
		if ar1[i] == ar2[j]:
			ar3.append(ar1[i])
		else:
			continue

print(ar3)
