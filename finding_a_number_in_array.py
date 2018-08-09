import random
li = [random.randint(1,100) for x in range(1,50)]
print(li)
for i in range(0,len(li)):
	for j in range(i+1,len(li)):
		if li[i]<=li[j]:
			li[i]=li[i]+li[j]
			li[j]=li[i]-li[j]
			li[i]=li[i]-li[j]
findn = 42
print(li)
j=0
k=len(li)
#method1
for i in range(j,k):
	mid = int((j+k)/2)
	print("mid: "+str(mid))
	if(findn == li[mid]):
		print("num : "+str(findn)+" at "+str(mid))
		break
	else:
		if findn>li[mid]:
			k = mid
		else:
			j = mid+1
#method2
for i in range(0,len(li)):
	if findn == li[i]:
		print("found 42 at "+str(i))
		break
