'''
Suppose various racing horses are their and given then the 1,2,3,4.... and their skills is given. Then we have to find 2 horses who have minimum difference 
in their skills.
p = [1,2,3,4,5,6]
s = [20,30,40,10,60,20]
a = []
'''
s = input()
s= [int(x) for x in s.split(" ")]
# s is the array for skills for the horses 
a = []
# a is the auxilliary array to calculate difference table
for i in range(len(s)):
    col = []
    for j in range(len(s)):
        col.insert(j,0)
    a.append(col)
for i in range(0,(len(s))):
    for j in range(0,len(s)):
        a[i].insert(j,s[i]-s[j])
for i in range(len(s)):
    for j in range(len(s)):
        if a[i][j]<0:
            a[i][j] = a[i][j]*(-1)
for i in range(0,len(s)):
    for j in range(0,int(len(s))):
        a[i].pop()        
# mn in minimum array containing minimum difference of skills between horses for each horse.
mn = []
for i in range(0,len(s)):
    m = 100
    for j in range(0,len(s)):
        if i==j:
            continue
        else:
            if m  > a[i][j]:
                m = a[i][j]
    mn.insert(i,m)
# calculate minimum of minimum found! 
print(min(mn))
