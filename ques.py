def closest(s, queries):
	result = []
	for i in range(1,len(queries)):
		index = queries[i]
		el = s[index]
		l = []
		for j in range(0,len(s)):
			if j == index:
				continue
			else:
				if s[j]==el:
					l.append(j)
		if len(l)==0:
			print("-1")
			result.append("-1")
		else:
			li=[]
			for k in l:
				li.append(abs(index-k))
			ind = li.index(min(li))
			print(l[ind])
			result.append(l[ind])
	return result
s = "sam"
q = [1,1]
print(closest(s,q))